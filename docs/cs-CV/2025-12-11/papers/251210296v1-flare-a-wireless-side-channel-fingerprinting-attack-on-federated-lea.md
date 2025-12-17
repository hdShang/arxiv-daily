---
layout: default
title: FLARE: A Wireless Side-Channel Fingerprinting Attack on Federated Learning
---

# FLARE: A Wireless Side-Channel Fingerprinting Attack on Federated Learning

**arXiv**: [2512.10296v1](https://arxiv.org/abs/2512.10296) | [PDF](https://arxiv.org/pdf/2512.10296.pdf)

**作者**: Md Nahid Hasan Shuvo, Moinul Hossain, Anik Mallik, Jeffrey Twigg, Fikadu Dagefu

---

## 💡 一句话要点

**提出FLARE侧信道指纹攻击，通过无线流量分析推断联邦学习模型架构**

**关键词**: `联邦学习` `侧信道攻击` `模型指纹识别` `无线流量分析` `深度学习安全`

## 📋 核心要点

1. 核心问题：联邦学习中模型架构信息可能通过加密无线流量泄露，威胁隐私安全
2. 方法要点：利用流量统计特征对CNN和RNN模型进行指纹识别，无需解密数据
3. 实验或效果：在闭集和开集场景下分别达到98%和91%的F1分数，验证攻击有效性

## 📄 摘要（原文）

> Federated Learning (FL) enables collaborative model training across distributed devices while safeguarding data and user privacy. However, FL remains susceptible to privacy threats that can compromise data via direct means. That said, indirectly compromising the confidentiality of the FL model architecture (e.g., a convolutional neural network (CNN) or a recurrent neural network (RNN)) on a client device by an outsider remains unexplored. If leaked, this information can enable next-level attacks tailored to the architecture. This paper proposes a novel side-channel fingerprinting attack, leveraging flow-level and packet-level statistics of encrypted wireless traffic from an FL client to infer its deep learning model architecture. We name it FLARE, a fingerprinting framework based on FL Architecture REconnaissance. Evaluation across various CNN and RNN variants-including pre-trained and custom models trained over IEEE 802.11 Wi-Fi-shows that FLARE achieves over 98% F1-score in closed-world and up to 91% in open-world scenarios. These results reveal that CNN and RNN models leak distinguishable traffic patterns, enabling architecture fingerprinting even under realistic FL settings with hardware, software, and data heterogeneity. To our knowledge, this is the first work to fingerprint FL model architectures by sniffing encrypted wireless traffic, exposing a critical side-channel vulnerability in current FL systems.

