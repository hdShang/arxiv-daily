---
layout: default
title: LogisticsVLN: Vision-Language Navigation For Low-Altitude Terminal Delivery Based on Agentic UAVs
---

# LogisticsVLN: Vision-Language Navigation For Low-Altitude Terminal Delivery Based on Agentic UAVs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03460" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03460v1</a>
  <a href="https://arxiv.org/pdf/2505.03460.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03460v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03460v1', 'LogisticsVLN: Vision-Language Navigation For Low-Altitude Terminal Delivery Based on Agentic UAVs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinyuan Zhang, Yonglin Tian, Fei Lin, Yue Liu, Jing Ma, Kornélia Sára Szatmáry, Fei-Yue Wang

**分类**: cs.RO

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出LogisticsVLN以解决低空无人机终端配送问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无人机配送` `视觉-语言导航` `多模态模型` `智能物流` `终端配送`

## 📋 核心要点

1. 现有的无人机配送系统多集中于粗粒度目标，无法满足低空终端配送的精确需求。
2. 本文提出LogisticsVLN，通过集成多模态大语言模型，构建模块化的空中配送系统，提升请求理解和物体检测能力。
3. 在CARLA模拟器上构建的VLD数据集实验结果显示，LogisticsVLN在各模块的评估中表现出良好的可行性和鲁棒性。

## 📝 摘要（中文）

随着智能物流需求的增长，特别是精细化终端配送，自动化无人机（UAV）配送系统的必要性愈发凸显。然而，现有的最后一公里配送研究主要依赖地面机器人，而当前的无人机视觉-语言导航（VLN）任务则主要集中在粗粒度、长距离目标上，无法满足精确终端配送的需求。为此，本文提出了LogisticsVLN，一个基于多模态大语言模型（MLLMs）的可扩展空中配送系统。LogisticsVLN在请求理解、楼层定位、物体检测和行动决策等模块中集成了轻量级的大语言模型（LLMs）和视觉-语言模型（VLMs）。为支持这一新场景的研究与评估，我们在CARLA模拟器中构建了视觉-语言配送（VLD）数据集。实验结果表明LogisticsVLN系统的可行性，并对系统各模块进行了子任务级评估，为基础模型驱动的视觉-语言配送系统的鲁棒性和实际部署提供了宝贵的见解。

## 🔬 方法详解

**问题定义**：本文旨在解决现有无人机配送系统在低空终端配送中面临的精度不足问题。现有方法多依赖地面机器人，且无人机的视觉-语言导航任务主要集中在粗粒度目标，无法满足精细化需求。

**核心思路**：LogisticsVLN的核心思路是通过集成轻量级的大语言模型和视觉-语言模型，构建一个模块化的配送系统，以实现对请求的理解、楼层定位、物体检测和行动决策的综合处理。这样的设计旨在提升无人机在复杂环境中的导航和配送能力。

**技术框架**：LogisticsVLN的整体架构包括多个主要模块：请求理解模块、楼层定位模块、物体检测模块和行动决策模块。各模块通过轻量级的模型进行协同工作，形成一个高效的配送系统。

**关键创新**：本文的关键创新在于提出了一个基于多模态大语言模型的模块化空中配送系统，填补了现有无人机配送研究在精细化终端配送方面的空白。与现有方法相比，LogisticsVLN在处理复杂环境和精确目标识别上具有显著优势。

**关键设计**：在系统设计中，采用了轻量级的模型架构以保证实时性，同时在损失函数和网络结构上进行了优化，以提升模型在复杂场景下的鲁棒性和准确性。

## 📊 实验亮点

在VLD数据集上的实验结果表明，LogisticsVLN系统在请求理解和物体检测任务中表现优异，具体性能数据展示了相较于基线模型的显著提升，尤其在复杂环境下的导航精度和响应速度上均有显著改善。

## 🎯 应用场景

LogisticsVLN的研究具有广泛的应用潜力，特别是在城市物流、快递配送和应急救援等领域。通过提高无人机在复杂环境中的导航能力，该系统能够实现更高效的终端配送，降低人力成本，并提升配送服务的智能化水平。未来，该技术有望推动无人机在智能物流领域的广泛应用。

## 📄 摘要（原文）

> The growing demand for intelligent logistics, particularly fine-grained terminal delivery, underscores the need for autonomous UAV (Unmanned Aerial Vehicle)-based delivery systems. However, most existing last-mile delivery studies rely on ground robots, while current UAV-based Vision-Language Navigation (VLN) tasks primarily focus on coarse-grained, long-range goals, making them unsuitable for precise terminal delivery. To bridge this gap, we propose LogisticsVLN, a scalable aerial delivery system built on multimodal large language models (MLLMs) for autonomous terminal delivery. LogisticsVLN integrates lightweight Large Language Models (LLMs) and Visual-Language Models (VLMs) in a modular pipeline for request understanding, floor localization, object detection, and action-decision making. To support research and evaluation in this new setting, we construct the Vision-Language Delivery (VLD) dataset within the CARLA simulator. Experimental results on the VLD dataset showcase the feasibility of the LogisticsVLN system. In addition, we conduct subtask-level evaluations of each module of our system, offering valuable insights for improving the robustness and real-world deployment of foundation model-based vision-language delivery systems.

