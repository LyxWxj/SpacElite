<template>
    <div class="resultsZone">
      <div v-if="responseData">
        <div ref="chart"></div>
      </div>
      <div v-if="Summery">{{ Summery }}</div>
    </div>
  </template>
  
  <script>
  import * as echarts from "echarts";
  import { mapState } from 'vuex';
  
  export default {
    data() {
      return {
        chartInstance: null,
      };
    },
    computed: {
      ...mapState(['responseData']),
    },
    watch: {
      responseData: {
        handler(newData) {
          this.updateChart();
        },
        deep: true,
      },
    },
    mounted() {
        this.$nextTick(() => {
            this.chartInstance = echarts.init(this.$refs.chart);
            this.updateChart();
        });
    },
    methods: {
      updateChart() {
        if (this.responseData) {
            const { type, Xs, Ys, Yname } = this.responseData;
            const chartTypes = {
                bar: {
                // 配置项...
                    title: {
                        text: this.type,
                    },
                    xAxis: {
                        data: this.Xs
                    },
                    yAxis: {},
                    series: [
                        {
                            name: this.Yname,
                            type: 'bar',
                            data: this.Ys,
                        }
                    ]
                },
                scatter: {
                // 配置项...
                    title: {
                        text: this.type,
                    },
                    xAxis: {
                        type: 'value',
                        scale: true,
                        data: this.Xs,
                    },
                    yAxis: {
                        type: 'value',
                        scale: true,
                    },
                    series: [
                        {
                            name: this.Yname,
                            type: 'scatter',
                            data: this.Ys,
                        }
                    ]
                },
                polyline: {
                    title: {
                        text: this.type,
                        },
                        xAxis: {
                            type: 'value',
                            scale: true,
                            data: this.Xs,
                        },
                        yAxis: {
                            type: 'value',
                            scale: true,
                        },
                        series: [
                            {
                                name: this.Yname,
                                type: 'line',
                                data: this.Ys,
                            }
                        ]
                },
            };
          const option = chartTypes[this.responseData.type];
          if (option) {
            this.chartInstance.setOption(option);
          }
        }
      },
    },
  };
  </script>