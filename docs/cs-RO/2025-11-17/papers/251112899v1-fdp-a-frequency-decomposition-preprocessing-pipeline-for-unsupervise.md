---
layout: default
title: FDP: A Frequency-Decomposition Preprocessing Pipeline for Unsupervised Anomaly Detection in Brain MRI
---

# FDP: A Frequency-Decomposition Preprocessing Pipeline for Unsupervised Anomaly Detection in Brain MRI

**arXiv**: [2511.12899v1](https://arxiv.org/abs/2511.12899) | [PDF](https://arxiv.org/pdf/2511.12899.pdf)

**作者**: Hao Li, Zhenfeng Zhuang, Jingyu Lin, Yu Liu, Yifei Chen, Qiong Peng, Lequan Yu, Liansheng Wang

---

## 💡 一句话要点

**提出频率分解预处理框架以提升脑MRI无监督异常检测性能**

**关键词**: `无监督异常检测` `脑MRI分析` `频率分解` `病理抑制` `重建方法`

## 📋 核心要点

1. 脑MRI异常检测面临解剖多样性和标注数据稀缺的挑战
2. 通过频率域分析，分离异常与正常解剖信号，实现病理抑制和结构保留
3. 集成现有方法，DICE分数提升17.63%，并在多基准上稳健改进

## 📄 摘要（原文）

> Due to the diversity of brain anatomy and the scarcity of annotated data, supervised anomaly detection for brain MRI remains challenging, driving the development of unsupervised anomaly detection (UAD) approaches. Current UAD methods typically utilize artificially generated noise perturbations on healthy MRIs to train generative models for normal anatomy reconstruction, enabling anomaly detection via residual mapping. However, such simulated anomalies lack the biophysical fidelity and morphological complexity characteristic of true clinical lesions. To advance UAD in brain MRI, we conduct the first systematic frequency-domain analysis of pathological signatures, revealing two key properties: (1) anomalies exhibit unique frequency patterns distinguishable from normal anatomy, and (2) low-frequency signals maintain consistent representations across healthy scans. These insights motivate our Frequency-Decomposition Preprocessing (FDP) framework, the first UAD method to leverage frequency-domain reconstruction for simultaneous pathology suppression and anatomical preservation. FDP can integrate seamlessly with existing anomaly simulation techniques, consistently enhancing detection performance across diverse architectures while maintaining diagnostic fidelity. Experimental results demonstrate that FDP consistently improves anomaly detection performance when integrated with existing methods. Notably, FDP achieves a 17.63% increase in DICE score with LDM while maintaining robust improvements across multiple baselines. The code is available at https://github.com/ls1rius/MRI_FDP.

