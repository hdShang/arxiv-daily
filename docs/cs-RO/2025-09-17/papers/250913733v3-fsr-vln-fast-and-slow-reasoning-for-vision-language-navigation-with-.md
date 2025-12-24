---
layout: default
title: "FSR-VLN: Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph"
---

# FSR-VLN: Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13733" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13733v3</a>
  <a href="https://arxiv.org/pdf/2509.13733.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13733v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13733v3', 'FSR-VLN: Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaolin Zhou, Tingyang Xiao, Liu Liu, Yucheng Wang, Maiyue Chen, Xinrui Meng, Xinjie Wang, Wei Feng, Wei Sui, Zhizhong Su

**分类**: cs.RO

**发布日期**: 2025-09-17 (更新: 2025-11-25)

**备注**: Demo video are available at https://horizonrobotics.github.io/robot_lab/fsr-vln/

---

## 💡 一句话要点

**提出FSR-VLN，结合分层多模态场景图与快慢推理，提升视觉语言导航性能。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言导航` `机器人导航` `分层场景图` `快慢推理` `多模态融合`

## 📋 核心要点

1. 现有视觉语言导航方法在长距离空间推理方面存在局限，导致成功率低且推理延迟高，尤其是在长距离导航任务中。
2. FSR-VLN结合分层多模态场景图(HMSG)与快慢导航推理(FSR)，实现从粗到细的渐进式目标检索与选择。
3. 实验结果表明，FSR-VLN在多个数据集上取得了SOTA性能，响应时间显著降低，并成功集成到人形机器人平台。

## 📝 摘要（中文）

视觉语言导航(VLN)是机器人系统中的一项基础挑战，在现实环境中部署具身智能体具有广泛的应用。为了解决现有方法在长距离空间推理上的局限性，以及成功率低、推理延迟高等问题，我们提出了FSR-VLN，一个结合分层多模态场景图(HMSG)与快慢导航推理(FSR)的视觉语言导航系统。HMSG提供了一种多模态地图表示，支持从粗粒度的房间级定位到细粒度的目标视图和物体识别的渐进式检索。基于HMSG，FSR首先执行快速匹配以高效地选择候选房间、视图和物体，然后应用VLM驱动的细化来进行最终目标选择。在由人形机器人收集的四个综合室内数据集上，我们评估了FSR-VLN，这些数据集包含87条涵盖各种物体类别的指令。FSR-VLN在所有数据集上都实现了最先进(SOTA)的性能，通过检索成功率(RSR)衡量，并且通过仅在快速直觉失败时激活慢速推理，与基于VLM的方法相比，在巡视视频上的响应时间减少了82%。此外，我们将FSR-VLN与Unitree-G1人形机器人上的语音交互、规划和控制模块集成，从而实现自然语言交互和实时导航。

## 🔬 方法详解

**问题定义**：现有视觉语言导航方法在处理长距离、复杂指令时，由于缺乏有效的空间推理能力，导致导航成功率低，且计算复杂度高，推理速度慢。尤其是在需要精确定位目标物体或位置时，现有方法难以兼顾准确性和效率。

**核心思路**：论文的核心思路是模拟人类的认知过程，采用“快慢推理”机制。首先通过快速匹配迅速缩小搜索范围，然后利用更精细的视觉语言模型进行精确判断。同时，引入分层多模态场景图，将环境信息组织成多粒度的结构，方便快速检索和推理。

**技术框架**：FSR-VLN系统主要包含两个核心模块：分层多模态场景图(HMSG)和快慢导航推理(FSR)。HMSG负责构建环境的多模态地图表示，包括房间级、视图级和物体级的信息。FSR模块首先利用快速匹配算法在HMSG中筛选候选目标，然后使用视觉语言模型(VLM)对候选目标进行细化和排序，最终选择最佳目标。整个流程可以概括为：指令输入 -> HMSG检索（快速匹配）-> VLM细化（慢速推理）-> 导航决策。

**关键创新**：该论文的关键创新在于提出了结合分层场景图和快慢推理的导航框架。与传统的端到端方法或单一推理模式相比，FSR-VLN能够更有效地利用环境信息，并在保证准确性的前提下显著提升推理速度。分层场景图的设计使得系统能够从粗到细地进行目标检索，而快慢推理机制则允许系统根据任务的复杂程度动态调整推理策略。

**关键设计**：HMSG采用多层结构，每一层对应不同的粒度级别（房间、视图、物体）。每一层都包含视觉、语言和空间信息。快速匹配算法基于简单的相似度度量，例如余弦相似度或欧氏距离。VLM细化阶段使用预训练的视觉语言模型，例如CLIP或ALIGN，对候选目标进行排序。损失函数的设计旨在平衡导航的准确性和效率，例如，可以采用交叉熵损失或排序损失。

## 📊 实验亮点

FSR-VLN在四个室内数据集上取得了SOTA性能，检索成功率(RSR)显著提升。更重要的是，与基于VLM的方法相比，FSR-VLN的响应时间减少了82%，这表明其快慢推理机制能够有效地降低计算复杂度，提升导航效率。在Unitree-G1人形机器人上的集成验证了该方法的实用性和可扩展性。

## 🎯 应用场景

FSR-VLN在机器人导航领域具有广泛的应用前景，例如家庭服务机器人、仓库物流机器人、安防巡逻机器人等。该技术可以帮助机器人在复杂环境中更准确、更高效地完成导航任务，提升用户体验。此外，该研究对于开发更智能、更自主的机器人系统具有重要的理论价值和实践意义。

## 📄 摘要（原文）

> Visual-Language Navigation (VLN) is a fundamental challenge in robotic systems, with broad applications for the deployment of embodied agents in real-world environments. Despite recent advances, existing approaches are limited in long-range spatial reasoning, often exhibiting low success rates and high inference latency, particularly in long-range navigation tasks. To address these limitations, we propose FSR-VLN, a vision-language navigation system that combines a Hierarchical Multi-modal Scene Graph (HMSG) with Fast-to-Slow Navigation Reasoning (FSR). The HMSG provides a multi-modal map representation supporting progressive retrieval, from coarse room-level localization to fine-grained goal view and object identification. Building on HMSG, FSR first performs fast matching to efficiently select candidate rooms, views, and objects, then applies VLM-driven refinement for final goal selection. We evaluated FSR-VLN across four comprehensive indoor datasets collected by humanoid robots, utilizing 87 instructions that encompass a diverse range of object categories. FSR-VLN achieves state-of-the-art (SOTA) performance in all datasets, measured by the retrieval success rate (RSR), while reducing the response time by 82% compared to VLM-based methods on tour videos by activating slow reasoning only when fast intuition fails. Furthermore, we integrate FSR-VLN with speech interaction, planning, and control modules on a Unitree-G1 humanoid robot, enabling natural language interaction and real-time navigation.

