---
layout: default
title: RED-F: Reconstruction-Elimination based Dual-stream Contrastive Forecasting for Multivariate Time Series Anomaly Prediction
---

# RED-F: Reconstruction-Elimination based Dual-stream Contrastive Forecasting for Multivariate Time Series Anomaly Prediction

**arXiv**: [2511.20044v1](https://arxiv.org/abs/2511.20044) | [PDF](https://arxiv.org/pdf/2511.20044.pdf)

**作者**: PengYu Chen, Xiaohou Shi, Yuan Chang, Yan Sun, Sajal K. Das

---

## 💡 一句话要点

**提出RED-F框架以解决多元时间序列中微弱异常前兆预测问题**

**关键词**: `多元时间序列` `异常预测` `重构消除` `双流对比` `对比预测` `时间序列分析`

## 📋 核心要点

1. 核心问题：现有方法在正常数据训练下，预测时易被正常模式主导，难以捕捉微弱异常前兆。
2. 方法要点：采用重构消除模型生成纯净基线，双流对比预测模型通过轨迹比较放大前兆信号。
3. 实验或效果：在六个真实数据集上验证，RED-F在异常预测任务中表现优越。

## 📄 摘要（原文）

> The proactive prediction of anomalies (AP) in mul- tivariate time series (MTS) is a critical challenge to ensure system dependability. The difficulty lies in identifying subtle anomaly precursors concealed within normal signals. However, existing unsupervised methods, trained exclusively on normal data, demonstrate a fundamental propensity to reconstruct normal patterns. Consequently, when confronted with weak precursors, their predictions are dominated by the normal pattern, submerging the very signal required for prediction. To contend with the limitation, we propose RED-F, a Reconstruction- Elimination based Dual-stream Contrastive Forecasting frame- work, comprising the Reconstruction-Elimination Model (REM) and the Dual-stream Contrastive Forecasting Model (DFM). The REM utilizes a hybrid time-frequency mechanism to mitigate the precursor, generating a purified, normal-pattern baseline. The DFM then receives this purified baseline and the original sequence which retains the precursor as parallel inputs. At the core of our framework, RED-F employs a contrastive forecast that transforms the difficult task of absolute signal detection into a simpler, more robust task of relative trajectory comparison by computing the divergence between these two predictive streams. This contrastive mechanism serves to amplify the faint precursor signal. Furthermore, the DFM is trained with a novel Multi-Series Prediction (MSP) objective, which leverages distant future con- text to enhance its predictive sensitivity. Extensive experiments on six real-world datasets demonstrate the superior capability of RED-F in anomaly prediction tasks.

