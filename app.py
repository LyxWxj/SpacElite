from flask import Flask, request, jsonify
from flask_cors import CORS
import src.algorithms as algo

def Barplot(data : dict):
    """
    data: {
        Xs: [str],
        Ys: [int]
    }
    """
    Xs = data['Xs']
    Ys = data['Ys']
    return jsonify({
        'type': 'bar',
        'event': 'plot',
        'Xs': Xs,
        'Ys': Ys,
        'Colors': 0,
        'Summery': 0,
    })

def ScatterPlot(data : dict):
    """
    data: {
        Xs: [int],
        Ys: [int]
    }
    """
    Xs = data['Xs']
    Ys = data['Ys']
    return jsonify({

        'type': 'scatter',
        'event': 'plot',
        'Xs': Xs,
        'Ys': Ys,
        'Xname': data['Xname'],
        'Yname': data['Yname'],
        'Colors': 0,
        'Summery': 0,
    })

def PolylinePlot(data : dict):
    """
    data: {
        Xs: [int],
        Ys: [int]
    }
    """
    Xs = data['Xs']
    Ys = data['Ys']
    return jsonify({
        'type': 'polyline',
        'event': 'plot',
        'Xs': Xs,
        'Ys': Ys,
        'Xname': data['Xname'],
        'Yname': data['Yname'],
        'Colors': 0,
        'Summery': 0,
    })


def DBSCAN(data: dict):
    """
    data: {
        Xs: [int],
        r: float,
        minPts: int
    }
    """
    Xs = data['Xs']
    r = data['r']
    minPts = data['minPts']
    return jsonify({
        'type': 'scatter',
        'event': 'cluster',
        'Xs': Xs,
        'Xname': data['Xname'],
        'Yname': data['Yname'],
        'Colors': algo.dbscan(Xs, r, minPts),
        'Summery': 0,
    })

def Kmeans(data: dict):
    """
    data: {
        Xs: [int],
        k: int
    }
    """
    Xs = data['Xs']
    k = data['k']
    distmeas = data['distmeas']
    return jsonify({
        'type': 'scatter',
        'event': 'cluster',
        'Xs': Xs,
        'Xname': data['Xname'],
        'Yname': data['Yname'],
        'Colors': algo.Kmeans(Xs, k, distmeas),
        'Summery': 0,
    })

def GaussianMixture(data: dict):
    """
    data: {
        Xs: [int],
        k: int
    }
    """
    Xs = data['Xs']
    k = data['k']
    return jsonify({
        'type': 'scatter',
        'event': 'cluster',
        'Xs': Xs,
        'Xname': data['Xname'],
        'Yname': data['Yname'],
        'Colors': algo.GaussianMixture(Xs, k),
        'Summery': 0,
    })

def SVM(data:dict):
    """
    data: {
        Xs: [int],
        Ys: [int],
        Xname: str,
        Yname: str,
        C: float,
        kernelfunc: str
    }
    """
    Xs = data['Xs']
    Ys = data['Ys']
    C = data['C']
    kernelfunc = data['kernelfunc']
    return jsonify({
        'type': 'scatter',
        'event': 'classification',
        'Xs': Xs,
        'Ys': algo.SVMClassification(Xs, Ys, Xs, C, kernelfunc),
        'Xname': data['Xname'],
        'Yname': data['Yname'],
        'Colors': 0,
        'Summery': 0,
    })

def DecisionTree(data:dict):
    """
    data : {
        Xs: [int],
        Ys: [int],
        Xname: str,
        Yname: str,
        criterion: str,
        splitter: str,
    }
    """
    Xs = data['Xs']
    Ys = data['Ys']
    criterion = data['criterion']
    splitter = data['splitter']
    return jsonify({
        'type': 'scatter',
        'event': 'classification',
        'Xs': Xs,
        'Ys': algo.DecisionTreeClassification(Xs, Ys, Xs, criterion, splitter),
        'Xname': data['Xname'],
        'Yname': data['Yname'],
        'Colors': 0,
        'Summery': 0,
    })


def LogisticRegression(data:dict):
    """
    data: {
        Xs: [int],
        Ys: [int],
        Xname: str,
        Yname: str,
    }
    """
    Xs = data['Xs']
    Ys = data['Ys']
    return jsonify({
        'type': 'scatter',
        'event': 'regression',
        'Xs': Xs,
        'Ys': algo.LogisticRegression(Xs, Ys, Xs),
        'Xname': data['Xname'],
        'Yname': data['Yname'],
        'Colors': 0,
        'Summery': 0,
    })

def SVR(data:dict):
    """
    data: {
        Xs: [int],
        Ys: [int],
        Xname: str,
        Yname: str,
        C: float,
        kernelfunc: str
    }
    """
    Xs = data['Xs']
    Ys = data['Ys']
    C = data['C']
    kernelfunc = data['kernelfunc']
    return jsonify({
        'type': 'scatter',
        'event': 'regression',
        'Xs': Xs,
        'Ys': algo.SVMRegression(Xs, Ys, Xs, C, kernelfunc),
        'Xname': data['Xname'],
        'Yname': data['Yname'],
        'Colors': 0,
        'Summery': 0,
    })


def RandomForest(data: dict):
    """
    data = {
        Xs: 
        Ys: 
        criterion: str
    }
    """
    Xs = data['Xs']
    Ys = data['Ys']
    criterion = data['criterion']
    return jsonify({
        'type': 'scatter',
        'event': 'regression',
        'Xs': Xs,
        'Ys': algo.RandomForestRegression(Xs, Ys, Xs, criterion),
        'Xname': data['Xname'],
        'Yname': data['Yname'],
        'Colors': 0,
        'Summery': 0,
    })


    




app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    requestFunc = data['request']
    res = eval(requestFunc)(data)
    return jsonify(res)

    
if __name__ == '__main__':
    app.run(port=5000)