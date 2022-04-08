# azureml_batch-endpoints_automl
Try managed batch endpoints of Azure Machine Learning
やりたいこと：AutoMLで学習したモデルをマネージドバッチエンドポイントにデプロイし推論環境を構成する

# Contents
・Python SDK による AutoML実行
- テーブルデータ (Titanic)
- 分類タスク
・GUIベースでのバッチエンドポイント実行
- 推論スクリプト: score.py (構築中、まだ動かない)

# Refs
- Docs: https://docs.microsoft.com/ja-jp/azure/machine-learning/how-to-use-batch-endpoints-studio
- Misc.
https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/batch/mnist/code/digit_identification.py
https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/machine-learning-pipelines/parallel-run/tabular-dataset-inference-iris.ipynb
https://docs.microsoft.com/ja-jp/cli/azure/ml/batch-endpoint?view=azure-cli-latest#az-ml-batch-endpoint-invoke

