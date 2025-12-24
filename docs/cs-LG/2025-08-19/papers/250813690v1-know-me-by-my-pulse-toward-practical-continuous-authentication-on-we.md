---
layout: default
title: "Know Me by My Pulse: Toward Practical Continuous Authentication on Wearable Devices via Wrist-Worn PPG"
---

# Know Me by My Pulse: Toward Practical Continuous Authentication on Wearable Devices via Wrist-Worn PPG

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13690" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13690v1</a>
  <a href="https://arxiv.org/pdf/2508.13690.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13690v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13690v1', 'Know Me by My Pulse: Toward Practical Continuous Authentication on Wearable Devices via Wrist-Worn PPG')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Shao, Zequan Liang, Ruoyu Zhang, Ruijie Fang, Ning Miao, Ehsan Kourkchi, Setareh Rafatirad, Houman Homayoun, Chongzhou Fang

**分类**: cs.CR, cs.LG

**发布日期**: 2025-08-19

**备注**: To be published in Network and Distributed System Security (NDSS) Symposium 2026

---

## 💡 一句话要点

**提出基于低频PPG信号的连续身份认证方法以解决可穿戴设备的安全性问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `生物特征认证` `光电容积脉搏波` `低频信号` `连续身份认证` `可穿戴设备` `深度学习` `鲁棒性`

## 📋 核心要点

1. 现有的生物特征认证方法多依赖于高频PPG信号和复杂深度模型，导致能耗和计算开销过大，限制了实际应用。
2. 本文提出了一种基于低频（25 Hz）多通道PPG信号的连续身份认证系统，利用Bi-LSTM网络提取身份特征，降低能耗。
3. 实验结果显示，系统在保持高准确率的同时，传感器功耗降低53%，并且在多种生理状态下表现出更强的鲁棒性。

## 📝 摘要（中文）

生物特征认证利用生理信号为可穿戴设备提供安全且用户友好的访问控制。尽管心电图（ECG）信号具有高辨别率，但其侵入式传感需求和不连续采集限制了其实用性。相较之下，光电容积脉搏波（PPG）信号支持连续、非侵入式认证，适合集成于腕部可穿戴设备。本文首次在智能手表We-Be Band上实现并评估了基于低频（25 Hz）多通道PPG信号的连续认证系统。我们的方法采用带注意力机制的双向长短期记忆网络（Bi-LSTM），从4通道PPG的短窗口中提取身份特征。通过对公共数据集和We-Be数据集的广泛评估，我们展示了强大的分类性能，平均测试准确率为88.11%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有高频PPG信号认证方法在能耗和计算开销上的不足，限制了其在实际可穿戴设备中的应用。

**核心思路**：提出基于低频（25 Hz）多通道PPG信号的认证方法，采用Bi-LSTM网络结合注意力机制提取身份特征，旨在实现低功耗且高效的身份认证。

**技术框架**：整体架构包括数据采集模块、特征提取模块和分类模块。数据采集模块负责获取4通道PPG信号，特征提取模块使用Bi-LSTM网络处理短时间窗口数据，分类模块进行身份识别。

**关键创新**：本研究的关键创新在于首次实现低频PPG信号的连续身份认证，显著降低了功耗，同时保持了高准确率，区别于传统高频方法。

**关键设计**：系统采用25 Hz的采样频率，减少了53%的传感器功耗；使用4通道PPG信号的4秒短窗口进行特征提取，训练过程中考虑了多种生理状态以提高模型的鲁棒性。

## 📊 实验亮点

实验结果表明，本文提出的系统在公共数据集和We-Be数据集上实现了88.11%的平均测试准确率，宏观F1-score为0.88，假接受率（FAR）为0.48%，假拒绝率（FRR）为11.77%，等错误率（EER）为2.76%。与512 Hz和128 Hz的设置相比，功耗分别降低了53%和19%。

## 🎯 应用场景

该研究的潜在应用领域包括智能手表、健康监测设备及其他可穿戴技术，能够为用户提供安全的身份认证方案。随着可穿戴设备的普及，低功耗的生物特征认证方法将提升用户体验并增强设备安全性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Biometric authentication using physiological signals offers a promising path toward secure and user-friendly access control in wearable devices. While electrocardiogram (ECG) signals have shown high discriminability, their intrusive sensing requirements and discontinuous acquisition limit practicality. Photoplethysmography (PPG), on the other hand, enables continuous, non-intrusive authentication with seamless integration into wrist-worn wearable devices. However, most prior work relies on high-frequency PPG (e.g., 75 - 500 Hz) and complex deep models, which incur significant energy and computational overhead, impeding deployment in power-constrained real-world systems. In this paper, we present the first real-world implementation and evaluation of a continuous authentication system on a smartwatch, We-Be Band, using low-frequency (25 Hz) multi-channel PPG signals. Our method employs a Bi-LSTM with attention mechanism to extract identity-specific features from short (4 s) windows of 4-channel PPG. Through extensive evaluations on both public datasets (PTTPPG) and our We-Be Dataset (26 subjects), we demonstrate strong classification performance with an average test accuracy of 88.11%, macro F1-score of 0.88, False Acceptance Rate (FAR) of 0.48%, False Rejection Rate (FRR) of 11.77%, and Equal Error Rate (EER) of 2.76%. Our 25 Hz system reduces sensor power consumption by 53% compared to 512 Hz and 19% compared to 128 Hz setups without compromising performance. We find that sampling at 25 Hz preserves authentication accuracy, whereas performance drops sharply at 20 Hz while offering only trivial additional power savings, underscoring 25 Hz as the practical lower bound. Additionally, we find that models trained exclusively on resting data fail under motion, while activity-diverse training improves robustness across physiological states.

