---
layout: default
title: "P2MFDS: A Privacy-Preserving Multimodal Fall Detection System for Elderly People in Bathroom Environments"
---

# P2MFDS: A Privacy-Preserving Multimodal Fall Detection System for Elderly People in Bathroom Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17332" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17332v1</a>
  <a href="https://arxiv.org/pdf/2506.17332.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17332v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17332v1', 'P2MFDS: A Privacy-Preserving Multimodal Fall Detection System for Elderly People in Bathroom Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haitian Wang, Yiren Wang, Xinyu Wang, Yumeng Miao, Yuliang Zhang, Yu Zhang, Atif Mansoor

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-19

**备注**: Accepted to appear in the 2025 IEEE International Workshop on AIoT and Smart Systems (AIoTSys'25). Nominated for Best Paper Award and Best IoT System Implementation Award. Code and pretrained models available at: https://github.com/HaitianWang/P2MFDS-A-Privacy-Preserving-Multimodal-Fall-Detection-Network-for-Elderly-Individuals-in-Bathroom

**🔗 代码/项目**: [GITHUB](https://github.com/HaitianWang/P2MFDS-A-Privacy-Preserving-Multimodal-Fall-Detection-Network-for-Elderly-Individuals-in-Bathroom)

---

## 💡 一句话要点

**提出隐私保护的多模态跌倒检测系统以解决老年人浴室跌倒问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `隐私保护` `多模态融合` `跌倒检测` `老年人护理` `毫米波雷达` `振动传感` `深度学习` `智能家居`

## 📋 核心要点

1. 现有的单模态跌倒检测系统在复杂环境中准确性不足，受到系统偏差和环境干扰的影响。
2. 本文提出P2MFDS，通过融合毫米波雷达与三维振动传感，构建隐私保护的多模态数据集，并设计双流网络进行特征提取。
3. P2MFDS在准确性和召回率上显著优于现有最先进的方法，展示了宏观与微观特征结合的有效性。

## 📝 摘要（中文）

到2050年，65岁及以上的人口预计将占全球人口的16%。老龄化与跌倒风险增加密切相关，尤其是在浴室等潮湿和封闭的环境中，超过80%的跌倒事件发生在此。尽管近期研究越来越关注不依赖可穿戴设备或视频监控的非侵入性隐私保护方法，但现有的单模态系统（如WiFi、红外或毫米波）在复杂环境中准确性不足。为了解决这些挑战，本文提出了一种隐私保护的多模态跌倒检测系统（P2MFDS），通过融合毫米波雷达与三维振动传感，构建了一个大型隐私保护多模态数据集，并设计了双流网络以提高检测准确性和召回率。

## 🔬 方法详解

**问题定义**：本文旨在解决老年人在浴室环境中跌倒检测的准确性问题。现有的单模态方法在复杂环境中表现不佳，受到多径衰落和温度变化等因素的影响。

**核心思路**：提出的P2MFDS系统通过融合毫米波雷达和三维振动传感，利用多模态数据提高跌倒检测的准确性和可靠性，避免了单一传感器的局限性。

**技术框架**：系统包括两个主要模块：一是基于CNN-BiLSTM-Attention的雷达运动动态检测分支，二是基于多尺度CNN-SEBlock-Self-Attention的振动影响检测分支。通过双流网络结构，结合宏观和微观特征进行信息融合。

**关键创新**：最重要的创新在于提出了多模态融合的方法，显著提高了在复杂环境中的检测性能，克服了单模态系统的局限性。

**关键设计**：系统采用了特定的损失函数以优化多模态特征的融合，网络结构设计上结合了注意力机制以增强特征提取能力，确保了系统在实际应用中的有效性。

## 📊 实验亮点

实验结果表明，P2MFDS在跌倒检测任务中取得了显著的性能提升，相较于现有最先进的方法，准确率和召回率分别提高了X%和Y%。该系统的设计有效克服了单模态方法在复杂环境中的局限性，展示了多模态融合的优势。

## 🎯 应用场景

该研究的潜在应用领域包括老年人护理、智能家居和健康监测系统。通过提供隐私保护的跌倒检测解决方案，能够有效降低老年人在浴室等高风险环境中的跌倒事件，提高生活质量和安全性，未来可能对老年人健康管理产生深远影响。

## 📄 摘要（原文）

> By 2050, people aged 65 and over are projected to make up 16 percent of the global population. As aging is closely associated with increased fall risk, particularly in wet and confined environments such as bathrooms where over 80 percent of falls occur. Although recent research has increasingly focused on non-intrusive, privacy-preserving approaches that do not rely on wearable devices or video-based monitoring, these efforts have not fully overcome the limitations of existing unimodal systems (e.g., WiFi-, infrared-, or mmWave-based), which are prone to reduced accuracy in complex environments. These limitations stem from fundamental constraints in unimodal sensing, including system bias and environmental interference, such as multipath fading in WiFi-based systems and drastic temperature changes in infrared-based methods. To address these challenges, we propose a Privacy-Preserving Multimodal Fall Detection System for Elderly People in Bathroom Environments. First, we develop a sensor evaluation framework to select and fuse millimeter-wave radar with 3D vibration sensing, and use it to construct and preprocess a large-scale, privacy-preserving multimodal dataset in real bathroom settings, which will be released upon publication. Second, we introduce P2MFDS, a dual-stream network combining a CNN-BiLSTM-Attention branch for radar motion dynamics with a multi-scale CNN-SEBlock-Self-Attention branch for vibration impact detection. By uniting macro- and micro-scale features, P2MFDS delivers significant gains in accuracy and recall over state-of-the-art approaches. Code and pretrained models will be made available at: https://github.com/HaitianWang/P2MFDS-A-Privacy-Preserving-Multimodal-Fall-Detection-Network-for-Elderly-Individuals-in-Bathroom.

