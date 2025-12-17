---
layout: default
title: Adaptive thresholding pattern for fingerprint forgery detection
---

# Adaptive thresholding pattern for fingerprint forgery detection

**arXiv**: [2511.15322v1](https://arxiv.org/abs/2511.15322) | [PDF](https://arxiv.org/pdf/2511.15322.pdf)

**作者**: Zahra Farzadpour, Masoumeh Azghani

---

## 💡 一句话要点

**提出自适应阈值模式以提升指纹伪造检测的抗失真能力**

**关键词**: `指纹伪造检测` `自适应阈值` `小波变换` `SVM分类` `抗失真能力` `图像处理`

## 📋 核心要点

1. 指纹活体检测系统易受伪造攻击，需区分真假指纹并抵抗噪声、像素缺失等失真
2. 方法基于小波变换和自适应阈值处理提取特征，使用SVM分类器进行检测
3. 实验显示在90%像素缺失和70x70块缺失场景下，准确率分别提升约8%和5%

## 📄 摘要（原文）

> Fingerprint liveness detection systems have been affected by spoofing, which is a severe threat for fingerprint-based biometric systems. Therefore, it is crucial to develop some techniques to distinguish the fake fingerprints from the real ones. The software based techniques can detect the fingerprint forgery automatically. Also, the scheme shall be resistant against various distortions such as noise contamination, pixel missing and block missing, so that the forgers cannot deceive the detector by adding some distortions to the faked fingerprint. In this paper, we propose a fingerprint forgery detection algorithm based on a suggested adaptive thresholding pattern. The anisotropic diffusion of the input image is passed through three levels of the wavelet transform. The coefficients of different layers are adaptively thresholded and concatenated to produce the feature vector which is classified using the SVM classifier. Another contribution of the paper is to investigate the effect of various distortions such as pixel missing, block missing, and noise contamination. Our suggested approach includes a novel method that exhibits improved resistance against a range of distortions caused by environmental phenomena or manipulations by malicious users. In quantitative comparisons, our proposed method outperforms its counterparts by approximately 8% and 5% in accuracy for missing pixel scenarios of 90% and block missing scenarios of size 70x70 , respectively. This highlights the novelty approach in addressing such challenges.

