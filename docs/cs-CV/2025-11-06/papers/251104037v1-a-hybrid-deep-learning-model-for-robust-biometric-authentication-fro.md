---
layout: default
title: A Hybrid Deep Learning Model for Robust Biometric Authentication from Low-Frame-Rate PPG Signals
---

# A Hybrid Deep Learning Model for Robust Biometric Authentication from Low-Frame-Rate PPG Signals

**arXiv**: [2511.04037v1](https://arxiv.org/abs/2511.04037) | [PDF](https://arxiv.org/pdf/2511.04037.pdf)

**作者**: Arfina Rahman, Mahesh Banavar

---

## 💡 一句话要点

**提出混合深度学习模型CVT-ConvMixer-LSTM，用于低帧率PPG信号的鲁棒生物认证**

**关键词**: `生物认证` `PPG信号处理` `混合深度学习` `时频分析` `运动伪影抑制`

## 📋 核心要点

1. 核心问题：PPG信号易受运动伪影和个体差异影响，需鲁棒特征提取
2. 方法要点：将PPG信号转换为时频图，结合CVT、ConvMixer和LSTM提取时空特征
3. 实验或效果：在46名受试者上实现98%认证准确率，验证模型抗噪和泛化能力

## 📄 摘要（原文）

> Photoplethysmography (PPG) signals, which measure changes in blood volume in
> the skin using light, have recently gained attention in biometric
> authentication because of their non-invasive acquisition, inherent liveness
> detection, and suitability for low-cost wearable devices. However, PPG signal
> quality is challenged by motion artifacts, illumination changes, and
> inter-subject physiological variability, making robust feature extraction and
> classification crucial. This study proposes a lightweight and cost-effective
> biometric authentication framework based on PPG signals extracted from
> low-frame-rate fingertip videos. The CFIHSR dataset, comprising PPG recordings
> from 46 subjects at a sampling rate of 14 Hz, is employed for evaluation. The
> raw PPG signals undergo a standard preprocessing pipeline involving baseline
> drift removal, motion artifact suppression using Principal Component Analysis
> (PCA), bandpass filtering, Fourier-based resampling, and amplitude
> normalization. To generate robust representations, each one-dimensional PPG
> segment is converted into a two-dimensional time-frequency scalogram via the
> Continuous Wavelet Transform (CWT), effectively capturing transient
> cardiovascular dynamics. We developed a hybrid deep learning model, termed
> CVT-ConvMixer-LSTM, by combining spatial features from the Convolutional Vision
> Transformer (CVT) and ConvMixer branches with temporal features from a Long
> Short-Term Memory network (LSTM). The experimental results on 46 subjects
> demonstrate an authentication accuracy of 98%, validating the robustness of the
> model to noise and variability between subjects. Due to its efficiency,
> scalability, and inherent liveness detection capability, the proposed system is
> well-suited for real-world mobile and embedded biometric security applications.

