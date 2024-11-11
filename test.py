import joblib

model = joblib.load('model_RandomForest.pkl')
if hasattr(model, '__getstate__'):
    print("Scikit-learn version (model state):", model.__getstate__().get('_sklearn_version', 'Version not found'))
