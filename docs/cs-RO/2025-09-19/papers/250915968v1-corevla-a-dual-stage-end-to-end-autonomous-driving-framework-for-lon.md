---
layout: default
title: "CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine"
---

# CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15968" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15968v1</a>
  <a href="https://arxiv.org/pdf/2509.15968.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15968v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15968v1', 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shiyu Fang, Yiming Cui, Haoyang Liang, Chen Lv, Peng Hang, Jian Sun

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-19

**🔗 代码/项目**: [GITHUB](https://github.com/FanGShiYuu/CoReVLA)

---

## 💡 一句话要点

**CoReVLA：通过收集与优化双阶段学习，提升长尾场景下端到端自动驾驶性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `长尾场景` `持续学习` `视觉-语言-动作模型` `直接偏好优化`

## 📋 核心要点

1. 现有自动驾驶系统在长尾场景下表现不佳，导致安全风险增加，亟需提升。
2. CoReVLA通过数据收集和行为优化双阶段学习，利用人类接管数据进行持续改进。
3. 实验表明，CoReVLA在长尾场景下显著提升了驾驶分数和成功率，优于现有方法。

## 📝 摘要（中文）

自动驾驶系统取得了显著进展，但在长尾、安全攸关场景中的性能仍然有限。这些罕见情况导致了不成比例的事故数量。视觉-语言-动作（VLA）模型具有强大的推理能力，并提供了一种潜在的解决方案，但其有效性受到高质量数据缺乏和在此类条件下低效学习的限制。为了应对这些挑战，我们提出了CoReVLA，一个持续学习的端到端自动驾驶框架，通过数据收集和行为优化的双阶段过程来提高长尾场景中的性能。首先，该模型在开源驾驶问答数据集的混合数据上进行联合微调，使其能够获得对驾驶场景的基础理解。接下来，CoReVLA部署在Cave Automatic Virtual Environment（CAVE）模拟平台中，从实时交互中收集驾驶员接管数据。每次接管都表明CoReVLA无法可靠处理的长尾场景。最后，该模型通过直接偏好优化（DPO）进行优化，使其能够直接从人类偏好中学习，从而避免手动设计的奖励导致的奖励利用。大量的开环和闭环实验表明，所提出的CoReVLA模型可以准确地感知驾驶场景并做出适当的决策。在Bench2Drive基准测试中，CoReVLA在长尾、安全攸关场景下实现了72.18的驾驶分数（DS）和50%的成功率（SR），优于最先进的方法7.96 DS和15% SR。此外，案例研究表明，该模型能够通过利用过去的接管经验，不断提高其在类似易错场景中的性能。所有代码和预处理数据集均可在https://github.com/FanGShiYuu/CoReVLA 获得。

## 🔬 方法详解

**问题定义**：论文旨在解决自动驾驶系统在长尾、安全攸关场景下性能不足的问题。现有方法难以有效处理这些罕见但高风险的情况，导致事故发生率较高。视觉-语言-动作（VLA）模型虽然具备潜力，但缺乏高质量的长尾数据和有效的学习机制来充分发挥其能力。

**核心思路**：论文的核心思路是通过持续学习的方式，利用模拟环境中的人类接管数据，不断优化VLA模型的驾驶策略。具体而言，首先让模型在通用驾驶数据集上学习基础知识，然后在模拟环境中部署，并记录人类驾驶员的接管行为。这些接管行为代表了模型无法处理的长尾场景，随后利用这些数据进行模型优化。

**技术框架**：CoReVLA框架包含两个主要阶段：数据收集（Collection）和行为优化（Refinement）。在数据收集阶段，CoReVLA部署在CAVE模拟环境中，与人类驾驶员进行交互。当CoReVLA无法做出安全决策时，人类驾驶员会接管控制，这些接管数据被记录下来。在行为优化阶段，CoReVLA利用直接偏好优化（DPO）算法，直接从人类偏好中学习，避免了手动设计奖励函数可能导致的奖励利用问题。

**关键创新**：CoReVLA的关键创新在于其双阶段的持续学习框架，以及利用人类接管数据进行模型优化的方法。与传统的基于规则或模仿学习的自动驾驶系统相比，CoReVLA能够不断适应新的长尾场景，并从人类驾驶员的经验中学习。DPO算法的使用也避免了手动设计奖励函数的困难和潜在的奖励利用问题。

**关键设计**：CoReVLA使用混合的开源驾驶问答数据集进行预训练，以获得对驾驶场景的基础理解。在行为优化阶段，DPO算法被用于直接从人类偏好中学习。具体的网络结构和参数设置在论文中可能有所描述，但摘要中未提供详细信息。损失函数主要基于DPO算法的偏好损失，旨在最大化模型对人类偏好的拟合程度。

## 📊 实验亮点

CoReVLA在Bench2Drive基准测试中取得了显著的性能提升，在长尾、安全攸关场景下实现了72.18的驾驶分数（DS）和50%的成功率（SR），优于最先进的方法7.96 DS和15% SR。案例研究也表明，该模型能够通过利用过去的接管经验，不断提高其在类似易错场景中的性能。

## 🎯 应用场景

CoReVLA的研究成果可应用于提升自动驾驶系统在复杂和罕见场景下的安全性，例如恶劣天气、突发交通状况等。通过持续学习和优化，自动驾驶汽车能够更好地适应各种驾驶环境，降低事故风险，最终实现更安全、可靠的自动驾驶。

## 📄 摘要（原文）

> Autonomous Driving (AD) systems have made notable progress, but their performance in long-tail, safety-critical scenarios remains limited. These rare cases contribute a disproportionate number of accidents. Vision-Language Action (VLA) models have strong reasoning abilities and offer a potential solution, but their effectiveness is limited by the lack of high-quality data and inefficient learning in such conditions. To address these challenges, we propose CoReVLA, a continual learning end-to-end autonomous driving framework that improves the performance in long-tail scenarios through a dual-stage process of data Collection and behavior Refinement. First, the model is jointly fine-tuned on a mixture of open-source driving QA datasets, allowing it to acquire a foundational understanding of driving scenarios. Next, CoReVLA is deployed within the Cave Automatic Virtual Environment (CAVE) simulation platform, where driver takeover data is collected from real-time interactions. Each takeover indicates a long-tail scenario that CoReVLA fails to handle reliably. Finally, the model is refined via Direct Preference Optimization (DPO), allowing it to learn directly from human preferences and thereby avoid reward hacking caused by manually designed rewards. Extensive open-loop and closed-loop experiments demonstrate that the proposed CoReVLA model can accurately perceive driving scenarios and make appropriate decisions. On the Bench2Drive benchmark, CoReVLA achieves a Driving Score (DS) of 72.18 and a Success Rate (SR) of 50%, outperforming state-of-the-art methods by 7.96 DS and 15% SR under long-tail, safety-critical scenarios. Furthermore, case studies demonstrate the model's ability to continually improve its performance in similar failure-prone scenarios by leveraging past takeover experiences. All codea and preprocessed datasets are available at: https://github.com/FanGShiYuu/CoReVLA

