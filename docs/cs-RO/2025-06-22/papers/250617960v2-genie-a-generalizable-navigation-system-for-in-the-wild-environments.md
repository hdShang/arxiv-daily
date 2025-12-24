---
layout: default
title: "GeNIE: A Generalizable Navigation System for In-the-Wild Environments"
---

# GeNIE: A Generalizable Navigation System for In-the-Wild Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17960" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17960v2</a>
  <a href="https://arxiv.org/pdf/2506.17960.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17960v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17960v2', 'GeNIE: A Generalizable Navigation System for In-the-Wild Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaming Wang, Diwen Liu, Jizhuo Chen, Jiaxuan Da, Nuowen Qian, Tram Minh Man, Harold Soh

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-22 (更新: 2025-10-18)

**备注**: Accepted to IEEE Robotics and Automation Letters (RAL), 2025. Jiaming Wang, Diwen Liu, and Jizhuo Chen contributed equally to this work

---

## 💡 一句话要点

**提出GeNIE以解决复杂环境下的导航问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `通用导航` `可通行性预测` `路径规划` `机器人导航` `复杂环境`

## 📋 核心要点

1. 现有导航方法在复杂和多变的环境中表现不佳，难以适应不同的地形和条件。
2. GeNIE通过结合通用可通行性预测模型和路径融合策略，提升了导航的稳定性和可靠性。
3. 在Earth Rover Challenge中，GeNIE以79%的得分领先第二名17%，且实现了全程无人干预，展现了其优越性。

## 📝 摘要（中文）

在非结构化的真实世界环境中，可靠的导航仍然是一个重大挑战，尤其是在多样化的地形、天气条件和传感器配置下。本文介绍了GeNIE（适用于野外环境的通用导航系统），这是一个为全球部署而设计的强大导航框架。GeNIE集成了基于SAM2的通用可通行性预测模型和一种新颖的路径融合策略，以增强在噪声和模糊环境中的规划稳定性。GeNIE在2025年ICRA的Earth Rover Challenge中部署，跨越六个国家和三个大洲进行评估，获得第一名，得分达到最大可能分数的79%，超出第二名团队17%，且整个比赛过程中没有一次人工干预。这些结果为稳健、通用的户外机器人导航设定了新的基准。我们将发布代码库、预训练模型权重和新整理的数据集，以支持未来的真实世界导航研究。

## 🔬 方法详解

**问题定义**：本文旨在解决在复杂和多变的真实环境中，现有导航系统在适应性和稳定性方面的不足，尤其是在多样化的地形和传感器配置下。

**核心思路**：GeNIE的核心思路是通过集成通用可通行性预测模型和创新的路径融合策略，增强导航系统在噪声和模糊环境中的规划能力，从而实现更可靠的导航。

**技术框架**：GeNIE的整体架构包括两个主要模块：通用可通行性预测模块和路径融合模块。前者负责评估环境的可通行性，后者则在此基础上进行路径规划和优化。

**关键创新**：GeNIE的关键创新在于其路径融合策略，该策略能够有效处理环境中的噪声和不确定性，显著提高了导航的稳定性和准确性，与传统方法相比具有本质的区别。

**关键设计**：在设计中，GeNIE采用了特定的损失函数以优化可通行性预测，并在网络结构上进行了调整，以适应不同的传感器输入和环境特征。

## 📊 实验亮点

GeNIE在Earth Rover Challenge中表现卓越，获得第一名，得分79%，超出第二名17%。其全程无人干预的表现，展示了该系统在复杂环境下的高可靠性和稳定性，树立了新的导航基准。

## 🎯 应用场景

GeNIE的研究成果具有广泛的应用潜力，特别是在无人驾驶、机器人探测和救援任务等领域。其强大的导航能力能够支持机器人在复杂和动态的环境中自主移动，提升任务执行的效率和安全性。未来，GeNIE有望在更多实际场景中得到应用，推动相关技术的发展。

## 📄 摘要（原文）

> Reliable navigation in unstructured, real-world environments remains a significant challenge for embodied agents, especially when operating across diverse terrains, weather conditions, and sensor configurations. In this paper, we introduce GeNIE (Generalizable Navigation System for In-the-Wild Environments), a robust navigation framework designed for global deployment. GeNIE integrates a generalizable traversability prediction model built on SAM2 with a novel path fusion strategy that enhances planning stability in noisy and ambiguous settings. We deployed GeNIE in the Earth Rover Challenge (ERC) at ICRA 2025, where it was evaluated across six countries spanning three continents. GeNIE took first place and achieved 79% of the maximum possible score, outperforming the second-best team by 17%, and completed the entire competition without a single human intervention. These results set a new benchmark for robust, generalizable outdoor robot navigation. We will release the codebase, pretrained model weights, and newly curated datasets to support future research in real-world navigation.

