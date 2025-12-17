---
layout: default
title: Real-time prediction of breast cancer sites using deformation-aware graph neural network
---

# Real-time prediction of breast cancer sites using deformation-aware graph neural network

**arXiv**: [2511.13082v1](https://arxiv.org/abs/2511.13082) | [PDF](https://arxiv.org/pdf/2511.13082.pdf)

**作者**: Kyunghyun Lee, Yong-Min Shin, Minwoo Shin, Jihun Kim, Sunghwan Lim, Won-Yong Shin, Kyungho Yoon

---

## 💡 一句话要点

**提出变形感知图神经网络以实时预测乳腺癌活检中的肿瘤位移**

**关键词**: `图神经网络` `乳腺癌活检` `变形预测` `实时推理` `有限元模拟`

## 📋 核心要点

1. 核心问题：间接MRI引导活检中，实时精确预测乳腺变形模型存在挑战。
2. 方法要点：结合个体有限元模型和图神经网络，处理表面位移与距离图数据。
3. 实验或效果：验证显示位移误差小于0.2毫米，计算速度提升超4000倍。

## 📄 摘要（原文）

> Early diagnosis of breast cancer is crucial, enabling the establishment of appropriate treatment plans and markedly enhancing patient prognosis. While direct magnetic resonance imaging-guided biopsy demonstrates promising performance in detecting cancer lesions, its practical application is limited by prolonged procedure times and high costs. To overcome these issues, an indirect MRI-guided biopsy that allows the procedure to be performed outside of the MRI room has been proposed, but it still faces challenges in creating an accurate real-time deformable breast model. In our study, we tackled this issue by developing a graph neural network (GNN)-based model capable of accurately predicting deformed breast cancer sites in real time during biopsy procedures. An individual-specific finite element (FE) model was developed by incorporating magnetic resonance (MR) image-derived structural information of the breast and tumor to simulate deformation behaviors. A GNN model was then employed, designed to process surface displacement and distance-based graph data, enabling accurate prediction of overall tissue displacement, including the deformation of the tumor region. The model was validated using phantom and real patient datasets, achieving an accuracy within 0.2 millimeters (mm) for cancer node displacement (RMSE) and a dice similarity coefficient (DSC) of 0.977 for spatial overlap with actual cancerous regions. Additionally, the model enabled real-time inference and achieved a speed-up of over 4,000 times in computational cost compared to conventional FE simulations. The proposed deformation-aware GNN model offers a promising solution for real-time tumor displacement prediction in breast biopsy, with high accuracy and real-time capability. Its integration with clinical procedures could significantly enhance the precision and efficiency of breast cancer diagnosis.

