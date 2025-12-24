---
layout: default
title: GeoLLaVA-8K: Scaling Remote-Sensing Multimodal Large Language Models to 8K Resolution
---

# GeoLLaVA-8K: Scaling Remote-Sensing Multimodal Large Language Models to 8K Resolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21375" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21375v2</a>
  <a href="https://arxiv.org/pdf/2505.21375.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21375v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21375v2', 'GeoLLaVA-8K: Scaling Remote-Sensing Multimodal Large Language Models to 8K Resolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fengxiang Wang, Mingshuo Chen, Yueying Li, Di Wang, Haotian Wang, Zonghao Guo, Zefan Wang, Boqi Shan, Long Lan, Yulin Wang, Hongzhen Wang, Wenjing Yang, Bo Du, Jing Zhang

**分类**: cs.CV

**发布日期**: 2025-05-27 (更新: 2025-11-04)

**备注**: NeurlPS 2025 Spotlight

---

## 💡 一句话要点

**提出GeoLLaVA-8K以解决超高分辨率遥感图像处理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `超高分辨率` `遥感图像` `多模态模型` `数据集构建` `token选择` `背景修剪` `模型训练`

## 📋 核心要点

1. 现有多模态基础模型在处理超高分辨率遥感图像时面临数据稀缺和token爆炸的挑战。
2. 本文提出了SuperRS-VQA和HighRS-VQA数据集，并通过背景token修剪和锚定token选择来减少内存占用。
3. GeoLLaVA-8K在XLRS-Bench上设定了新的性能基准，展示了显著的性能提升。

## 📝 摘要（中文）

超高分辨率遥感图像为地球观测提供了宝贵数据，但现有多模态基础模型面临两个主要瓶颈：一是超高分辨率训练数据的稀缺，二是由于图像尺寸大导致的token爆炸。为了解决数据稀缺问题，本文引入了SuperRS-VQA和HighRS-VQA这两个最高分辨率的视觉-语言数据集，涵盖22个真实世界对话任务。为缓解token爆炸，研究发现遥感图像中关键信息集中在少量对象中心token中，去除背景token（如海洋或森林）反而能提高性能。基于此，提出了背景token修剪和锚定token选择两种策略，最终推出GeoLLaVA-8K，这是第一个能够处理高达8K×8K分辨率输入的遥感专用多模态大语言模型。

## 🔬 方法详解

**问题定义**：本文旨在解决超高分辨率遥感图像处理中的数据稀缺和token爆炸问题。现有方法在处理大尺寸图像时，往往面临内存不足和性能下降的困境。

**核心思路**：通过引入SuperRS-VQA和HighRS-VQA数据集，提供高质量的训练数据，同时采用背景token修剪和锚定token选择策略，减少冗余信息，提高模型性能。

**技术框架**：GeoLLaVA-8K基于LLaVA框架构建，整体架构包括数据预处理、token选择、模型训练和评估等主要模块。数据预处理阶段重点在于生成高分辨率的视觉-语言对，token选择阶段则通过分析图像内容来优化输入。

**关键创新**：最重要的创新在于提出了背景token修剪和锚定token选择两种策略，这与现有方法相比，显著减少了内存占用，同时保留了关键信息。

**关键设计**：在模型训练中，采用了特定的损失函数以优化视觉和语言的对齐，同时在网络结构上进行了调整，以适应高分辨率输入的特性。

## 📊 实验亮点

GeoLLaVA-8K在XLRS-Bench上设定了新的性能基准，展示了在处理8K分辨率输入时，相较于现有模型有显著的性能提升，具体提升幅度未知。

## 🎯 应用场景

该研究的潜在应用领域包括环境监测、城市规划、农业管理等，能够为遥感数据的分析和决策提供更高效的工具。未来，GeoLLaVA-8K有望推动遥感技术在各行各业的广泛应用，提升数据处理的智能化水平。

## 📄 摘要（原文）

> Ultra-high-resolution (UHR) remote sensing (RS) imagery offers valuable data for Earth observation but pose challenges for existing multimodal foundation models due to two key bottlenecks: (1) limited availability of UHR training data, and (2) token explosion caused by the large image size. To address data scarcity, we introduce SuperRS-VQA (avg. 8,376$\times$8,376) and HighRS-VQA (avg. 2,000$\times$1,912), the highest-resolution vision-language datasets in RS to date, covering 22 real-world dialogue tasks. To mitigate token explosion, our pilot studies reveal significant redundancy in RS images: crucial information is concentrated in a small subset of object-centric tokens, while pruning background tokens (e.g., ocean or forest) can even improve performance. Motivated by these findings, we propose two strategies: Background Token Pruning and Anchored Token Selection, to reduce the memory footprint while preserving key semantics.Integrating these techniques, we introduce GeoLLaVA-8K, the first RS-focused multimodal large language model capable of handling inputs up to 8K$\times$8K resolution, built on the LLaVA framework. Trained on SuperRS-VQA and HighRS-VQA, GeoLLaVA-8K sets a new state-of-the-art on the XLRS-Bench.

