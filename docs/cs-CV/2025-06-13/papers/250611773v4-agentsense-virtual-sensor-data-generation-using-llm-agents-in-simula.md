---
layout: default
title: "AgentSense: Virtual Sensor Data Generation Using LLM Agents in Simulated Home Environments"
---

# AgentSense: Virtual Sensor Data Generation Using LLM Agents in Simulated Home Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11773" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11773v4</a>
  <a href="https://arxiv.org/pdf/2506.11773.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11773v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11773v4', 'AgentSense: Virtual Sensor Data Generation Using LLM Agents in Simulated Home Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zikang Leng, Megha Thukral, Yaqi Liu, Hrudhai Rajasekhar, Shruthi K. Hiremath, Jiaman He, Thomas Plötz

**分类**: cs.CV, cs.HC

**发布日期**: 2025-06-13 (更新: 2025-11-11)

**备注**: Accepted by AAAI 2026

**🔗 代码/项目**: [GITHUB](https://github.com/ZikangLeng/AgentSense)

---

## 💡 一句话要点

**提出AgentSense以解决智能家居中缺乏多样化标注数据的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人类活动识别` `虚拟传感器` `具身AI` `大型语言模型` `数据生成` `智能家居` `模拟环境`

## 📋 核心要点

1. 现有的HAR系统面临缺乏大规模且多样化的标注数据的问题，家庭环境的复杂性使得数据收集更加困难。
2. 本文提出AgentSense，通过具身AI代理在模拟智能家居中生成虚拟传感器数据，利用LLM指导代理行为。
3. 实验结果表明，基于生成数据预训练的模型在多个真实数据集上表现优异，尤其在资源有限的情况下提升显著。

## 📝 摘要（中文）

在智能家居中，开发稳健且具有普适性的人的活动识别（HAR）系统面临着缺乏大规模多样化标注数据的挑战。家庭布局、传感器配置和个体行为的变化进一步加剧了这一问题。为了解决这一问题，本文提出了AgentSense，一个虚拟数据生成管道，利用具身AI代理在模拟环境中执行日常活动。通过大型语言模型（LLM），生成多样化的合成角色和基于环境的真实活动，这些活动被细分为精细的动作，并在扩展的VirtualHome模拟器中执行，记录代理的活动。我们的研究表明，使用生成的数据预训练的模型在五个真实HAR数据集上表现优于基线，尤其是在低资源环境下。此外，将生成的虚拟传感器数据与少量真实数据结合，能够达到与全真实数据集训练相当的性能。这些结果突显了LLM引导的具身代理在HAR领域中进行可扩展且经济高效的传感器数据生成的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决智能家居中缺乏多样化标注数据的问题。现有方法在家庭布局、传感器配置和个体行为的多样性方面存在不足，导致HAR系统的鲁棒性和普适性受到限制。

**核心思路**：论文的核心思路是利用具身AI代理在模拟环境中执行日常活动，通过大型语言模型（LLM）生成多样化的合成角色和真实的活动。这种设计使得生成的数据能够反映真实世界的多样性，同时保护隐私。

**技术框架**：整体架构包括虚拟代理、LLM生成的行为指导、扩展的VirtualHome模拟器和虚拟环境传感器。代理在模拟环境中执行细分的日常活动，传感器记录其行为，形成丰富的传感器数据。

**关键创新**：最重要的技术创新在于结合LLM与具身AI代理生成虚拟传感器数据，这与传统的基于真实数据的HAR系统有本质区别，能够在缺乏真实数据的情况下生成高质量的训练数据。

**关键设计**：在关键设计上，采用了虚拟环境中的多种传感器配置，确保生成的数据能够覆盖不同的家庭场景和活动类型。此外，模型的训练过程中使用了特定的损失函数，以优化生成数据的质量和多样性。

## 📊 实验亮点

实验结果显示，基于AgentSense生成的数据预训练的模型在五个真实HAR数据集上表现优于基线，尤其在低资源设置下，性能提升显著。此外，将生成的虚拟传感器数据与少量真实数据结合，能够达到与全真实数据集训练相当的性能，展示了该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用场景包括智能家居监控、老年人护理和智能助手等领域。通过生成多样化的传感器数据，HAR系统能够更好地适应不同的家庭环境和用户行为，从而提高智能家居的安全性和便利性。未来，该方法有望推动HAR技术的广泛应用，尤其是在数据稀缺的情况下。

## 📄 摘要（原文）

> A major challenge in developing robust and generalizable Human Activity Recognition (HAR) systems for smart homes is the lack of large and diverse labeled datasets. Variations in home layouts, sensor configurations, and individual behaviors further exacerbate this issue. To address this, we leverage the idea of embodied AI agents -- virtual agents that perceive and act within simulated environments guided by internal world models. We introduce AgentSense, a virtual data generation pipeline in which agents live out daily routines in simulated smart homes, with behavior guided by Large Language Models (LLMs). The LLM generates diverse synthetic personas and realistic routines grounded in the environment, which are then decomposed into fine-grained actions. These actions are executed in an extended version of the VirtualHome simulator, which we augment with virtual ambient sensors that record the agents' activities. Our approach produces rich, privacy-preserving sensor data that reflects real-world diversity. We evaluate AgentSense on five real HAR datasets. Models pretrained on the generated data consistently outperform baselines, especially in low-resource settings. Furthermore, combining the generated virtual sensor data with a small amount of real data achieves performance comparable to training on full real-world datasets. These results highlight the potential of using LLM-guided embodied agents for scalable and cost-effective sensor data generation in HAR. Our code is publicly available at https://github.com/ZikangLeng/AgentSense.

