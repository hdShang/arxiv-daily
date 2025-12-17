---
layout: default
title: OpenVLN: Open-world Aerial Vision-Language Navigation
---

# OpenVLN: Open-world Aerial Vision-Language Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.06182" class="toolbar-btn" target="_blank">📄 arXiv: 2511.06182v2</a>
  <a href="https://arxiv.org/pdf/2511.06182.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06182v2" onclick="toggleFavorite(this, '2511.06182v2', 'OpenVLN: Open-world Aerial Vision-Language Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peican Lin, Gan Sun, Chenxi Liu, Fazeng Li, Weihong Ren, Yang Cong

**分类**: cs.RO

**发布日期**: 2025-11-09 (更新: 2025-11-21)

**备注**: Content: 8 pages 4 figures, conference paper under review

---

## 💡 一句话要点

**提出OpenVLN框架，解决开放世界空中视觉-语言导航中的长程规划问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉-语言导航` `无人机导航` `强化学习` `长程规划` `开放世界`

## 📋 核心要点

1. 现有地面视觉-语言导航方法难以直接应用于复杂的户外空中环境，面临数据获取和长程轨迹规划的挑战。
2. OpenVLN框架通过强化学习优化VLM，并结合长程规划器，实现数据高效的语言引导无人机导航。
3. 实验表明，OpenVLN在成功率等指标上显著优于基线方法，验证了其在复杂空中环境中的有效性。

## 📝 摘要（中文）

本文提出了一种数据高效的开放世界空中视觉-语言导航（OpenVLN）框架，旨在解决无人机在复杂户外环境中执行语言引导飞行时面临的数据获取挑战和长程轨迹规划需求。该框架通过重新配置强化学习框架来优化视觉-语言模型（VLM），利用基于规则的策略在有限的训练数据下高效地微调VLM。同时，引入长程规划器，通过基于价值的奖励动态生成精确的无人机动作，用于轨迹合成。在TravelUAV基准上进行了充分的导航实验，结果表明，该方法在成功率、预言成功率和路径长度加权成功率方面均优于基线方法，验证了其在复杂空中环境中进行长程无人机导航的有效性。

## 🔬 方法详解

**问题定义**：现有的视觉-语言导航（VLN）方法主要集中在地面环境，难以直接应用于复杂的户外空中环境。在空中环境中，数据获取更加困难，且无人机需要进行长程轨迹规划，这给空中VLN带来了新的挑战。现有方法在数据效率和长程规划能力方面存在不足。

**核心思路**：本文的核心思路是利用强化学习来优化视觉-语言模型（VLM），使其能够更好地适应无人机导航任务。同时，引入一个长程规划器，通过基于价值的奖励来动态生成无人机的动作，从而实现长程轨迹规划。通过这种方式，可以在有限的数据下实现高效的空中VLN。

**技术框架**：OpenVLN框架主要包含两个模块：基于强化学习的VLM优化模块和长程规划器模块。首先，利用基于规则的策略生成的数据来微调VLM，使其能够理解语言指令并感知环境。然后，长程规划器根据VLM的输出和环境信息，通过基于价值的奖励来生成无人机的动作序列，从而实现长程轨迹规划。整个框架通过强化学习进行端到端训练。

**关键创新**：该方法的主要创新点在于将强化学习与VLM相结合，并引入长程规划器，从而实现了数据高效的空中VLN。与传统的VLN方法相比，该方法能够在有限的数据下实现更好的性能，并且能够处理长程轨迹规划问题。

**关键设计**：在VLM优化模块中，使用了基于规则的策略来生成训练数据，从而减少了对大量真实数据的依赖。在长程规划器中，使用了基于价值的奖励函数来指导无人机的动作选择。具体的奖励函数设计需要根据具体的任务进行调整。此外，网络结构的选择和参数设置也会影响最终的性能。

## 📊 实验亮点

实验结果表明，OpenVLN框架在TravelUAV基准测试中取得了显著的性能提升。具体而言，成功率提高了4.34%，预言成功率提高了6.19%，路径长度加权成功率提高了4.07%。这些结果表明，OpenVLN框架在复杂空中环境中进行长程无人机导航方面具有显著优势，优于现有的基线方法。

## 🎯 应用场景

OpenVLN框架可应用于无人机自主导航、环境监测、搜索救援、物流配送等领域。该研究能够提升无人机在复杂环境下的自主性和智能化水平，降低对人工干预的依赖，具有重要的实际应用价值和广阔的发展前景。未来可进一步探索在更复杂、动态环境下的应用，并结合其他传感器信息，提升系统的鲁棒性和可靠性。

## 📄 摘要（原文）

> Vision-language models (VLMs) have been widely-applied in ground-based vision-language navigation (VLN). However, the vast complexity of outdoor aerial environments compounds data acquisition challenges and imposes long-horizon trajectory planning requirements on Unmanned Aerial Vehicles (UAVs), introducing novel complexities for aerial VLN. To address these challenges, we propose a data-efficient Open-world aerial Vision-Language Navigation (i.e., OpenVLN) framework, which could execute language-guided flight with limited data constraints and enhance long-horizon trajectory planning capabilities in complex aerial environments. Specifically, we reconfigure a reinforcement learning framework to optimize the VLM for UAV navigation tasks, which can efficiently fine-tune VLM by using rule-based policies under limited training data. Concurrently, we introduce a long-horizon planner for trajectory synthesis that dynamically generates precise UAV actions via value-based rewards. To the end, we conduct sufficient navigation experiments on the TravelUAV benchmark with dataset scaling across diverse reward settings. Our method demonstrates consistent performance gains of up to 4.34% in Success Rate, 6.19% in Oracle Success Rate, and 4.07% in Success weighted by Path Length over baseline methods, validating its deployment efficacy for long-horizon UAV navigation in complex aerial environments.

