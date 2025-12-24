---
layout: default
title: Task-Oriented Semantic Communication in Large Multimodal Models-based Vehicle Networks
---

# Task-Oriented Semantic Communication in Large Multimodal Models-based Vehicle Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02413" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02413v1</a>
  <a href="https://arxiv.org/pdf/2505.02413.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02413v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02413v1', 'Task-Oriented Semantic Communication in Large Multimodal Models-based Vehicle Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Baoxia Du, Hongyang Du, Dusit Niyato, Ruidong Li

**分类**: cs.AI

**发布日期**: 2025-05-05

**DOI**: [10.1109/TMC.2025.3564543](https://doi.org/10.1109/TMC.2025.3564543)

---

## 💡 一句话要点

**提出基于LMM的任务导向语义通信框架以提升车辆网络性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `语义通信` `车辆网络` `视觉问答` `用户注意力` `资源优化` `智能交通`

## 📋 核心要点

1. 现有的语义通信方法在多模态信息处理和资源利用方面存在不足，难以满足复杂车辆网络的需求。
2. 提出了一种基于LMM的任务导向语义通信框架，通过优化图像处理和用户注意力评估来提升通信效率。
3. 实验结果显示，在信噪比为12dB和10dB的情况下，准确率分别提高了13.4%和33.1%，验证了框架的有效性。

## 📝 摘要（中文）

任务导向的语义通信已成为提升各种通信场景性能的基础方法。尽管生成式人工智能（GenAI）在语义通信设计中取得了进展，但大型多模态模型（LMM）的潜力尚未得到充分探索。本文研究了基于LMM的车辆AI助手，提出了一种任务导向的语义通信框架，以促进用户与云服务器之间的高效交互。通过优化LLaVA的图像切片，选择性关注用户最感兴趣的区域，减少计算需求并缩短响应时间。此外，结合客观和主观用户注意力评估图像块的重要性，调整传输语义信息的能量使用，从而优化资源利用，确保关键信息的精确传输。构建了一个交通场景的视觉问答（VQA）数据集进行有效性评估，实验结果表明，在相同信道条件下，该框架显著提高了回答问题的准确性，尤其在信噪比（SNR）较低的环境中表现优异。

## 🔬 方法详解

**问题定义**：本文旨在解决现有语义通信方法在多模态信息处理和资源利用上的不足，特别是在车辆网络中如何高效传输关键信息的问题。

**核心思路**：通过引入大型多模态模型（LMM），结合用户的注意力信息，优化图像切片处理，从而减少计算负担并提升响应速度。

**技术框架**：整体架构包括用户输入、图像处理模块、语义信息传输模块和云服务器响应模块。用户输入通过LLaVA进行处理，优化后的图像切片将被用于语义信息的传输。

**关键创新**：最重要的创新在于结合了客观与主观的用户注意力评估，动态调整图像块的传输能量，从而优化资源利用，确保关键信息的准确传输。

**关键设计**：在参数设置上，采用了基于用户反馈的动态调整机制，损失函数设计考虑了信息传输的准确性和效率，网络结构上则通过LLaVA实现了多模态信息的融合与处理。

## 📊 实验亮点

实验结果表明，提出的语义通信框架在相同信道条件下显著提高了问答准确性，尤其在信噪比为12dB和10dB时，准确率分别提升了13.4%和33.1%。这一成果展示了该框架在低信噪比环境下的优越性能。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、自动驾驶车辆和车联网（V2X）通信等。通过提升车辆网络中的语义通信效率，可以显著改善用户体验和系统响应速度，推动智能交通技术的发展与应用。

## 📄 摘要（原文）

> Task-oriented semantic communication has emerged as a fundamental approach for enhancing performance in various communication scenarios. While recent advances in Generative Artificial Intelligence (GenAI), such as Large Language Models (LLMs), have been applied to semantic communication designs, the potential of Large Multimodal Models (LMMs) remains largely unexplored. In this paper, we investigate an LMM-based vehicle AI assistant using a Large Language and Vision Assistant (LLaVA) and propose a task-oriented semantic communication framework to facilitate efficient interaction between users and cloud servers. To reduce computational demands and shorten response time, we optimize LLaVA's image slicing to selectively focus on areas of utmost interest to users. Additionally, we assess the importance of image patches by combining objective and subjective user attention, adjusting energy usage for transmitting semantic information. This strategy optimizes resource utilization, ensuring precise transmission of critical information. We construct a Visual Question Answering (VQA) dataset for traffic scenarios to evaluate effectiveness. Experimental results show that our semantic communication framework significantly increases accuracy in answering questions under the same channel conditions, performing particularly well in environments with poor Signal-to-Noise Ratios (SNR). Accuracy can be improved by 13.4% at an SNR of 12dB and 33.1% at 10dB, respectively.

