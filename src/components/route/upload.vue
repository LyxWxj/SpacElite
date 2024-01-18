<template>
<Transition appear>
  <div class="upload">
    <div class="uploadbox">
        <div class="uploadAndhint">
            <div class="inputup" id="inputup">
                <div class="Uploaddiv"> 
                    <form id="updata">
                        <a href="javascript:;">
                            {{ $t('message.clickUpload')}}
                            <input id="fileopcti" @change="handleFileUpload" class="fileopcti" type="file" ref="file" name="dataFile" value accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet">
                        </a>
                        <label id="labelfiles">{{ $t('message.dragUpload')}}</label>
                    </form>
                    <div class="hint">
                        <span>{{ $t('message.fileSupport') }}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="example">
      <span style="align: left;">{{ $t('message.exampleTip') }}</span>
      <img class="examplechart" src="../../assets/example.svg"/>
    </div>
  </div>
</Transition>
<Transition appear>
<div class="previewBox">
  <div class="previewTitle">
    <span>{{ $t('message.preview') }}</span>
  </div>
  <div class="previewTable">
    <table v-if="previewData && isActive">
      <thead>
        <tr>
          <th v-for="(value, key) in this.$store.state.fileData[0]" :key="key">
            {{ value }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in this.$store.state.fileData.slice(1)" :key="index">
          <td v-for="(value, key) in row" :key="key">
            {{ value }}
          </td>
        </tr>
      </tbody>
  </table>
  </div>
</div>
</Transition>
</template>

<script lang="js">

</script>

<style scoped>
@import './CSS/uploadfile.css';
</style>


<script lang="js">
import Papa from 'papaparse';
import * as xlsx from 'xlsx/xlsx.mjs';


export default {
  data() {
    return {
      previewData: null,
      isActive: false,
    }
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      this.readFile(file).then(data => {
        if (file.type === 'text/csv') {
          const parsedData = Papa.parse(data, { header: true }).data;
          this.previewData = parsedData;
          this.$store.commit('setfileData', parsedData);
        } else if (file.type === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') {
          const workbook = xlsx.read(data, {type: 'binary'});
          const sheetName = workbook.SheetNames[0];
          const worksheet = workbook.Sheets[sheetName];
          const parsedData = xlsx.utils.sheet_to_json(worksheet, {header: 1});
          this.$store.commit('setfileData', parsedData);
          this.previewData = parsedData;
        }
        this.isActive = true;
        this.$store.commit('setHasUploadedFile', true);
      });
    },
    readFile(file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = (e) => {
          resolve(e.target.result);
        };
        reader.onerror = (e) => {
          reject(e);
        };
        reader.readAsBinaryString(file);
      });
    },
    dropFile(e) {
      e.preventDefault();
      const files = e.dataTransfer.files;
      if (files.length > 0) {
        this.$refs.file.files = files;
        this.handleFileUpload();
      }
    },
  },
  mounted() {
    this.previewData = this.$store.state.fileData;
    if (this.previewData) {
      this.isActive = true;
    }
  },
};
</script>