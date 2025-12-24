---
layout: default
title: "DTCCL: Disengagement-Triggered Contrastive Continual Learning for Autonomous Bus Planners"
---

# DTCCL: Disengagement-Triggered Contrastive Continual Learning for Autonomous Bus Planners

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.18988" class="toolbar-btn" target="_blank">📄 arXiv: 2512.18988v1</a>
  <a href="https://arxiv.org/pdf/2512.18988.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.18988v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.18988v1', 'DTCCL: Disengagement-Triggered Contrastive Continual Learning for Autonomous Bus Planners')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanding Yang, Weitao Zhou, Jinhai Wang, Xiaomin Guo, Junze Wen, Xiaolong Liu, Lang Ding, Zheng Fu, Jinyu Miao, Kun Jiang, Diange Yang

**分类**: cs.RO

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出DTCCL框架，通过脱离事件触发的对比持续学习提升自动驾驶巴士规划策略。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自动驾驶` `持续学习` `对比学习` `数据增强` `脱离事件` `规划策略` `云边协同`

## 📋 核心要点

1. 现有模仿学习方法难以有效利用自动驾驶脱离数据，易于过拟合，导致策略改进受限。
2. DTCCL框架通过脱离事件触发数据增强，利用对比学习区分安全与不安全行为，实现持续策略优化。
3. 实验表明，DTCCL相较于直接重训练，在城市公交路线上整体规划性能提升了48.6%。

## 📝 摘要（中文）

自动驾驶巴士在固定路线上运行，但必须在开放、动态的城市环境中运行。这些路线上的脱离事件通常在地理位置上集中，并且通常由高度交互区域中的规划器故障引起。使用传统的模仿学习很难纠正此类策略级别的故障，因为模仿学习很容易过度拟合稀疏的脱离数据。为了解决这个问题，本文提出了一种脱离触发的对比持续学习（DTCCL）框架，使自动驾驶巴士能够通过实际操作来改进规划策略。每次脱离都会触发基于云的数据增强，通过扰动周围的智能体同时保留路线上下文来生成正样本和负样本。对比学习改进策略表示，以更好地区分安全和不安全的行为，并且在没有人工监督的情况下，在云边循环中应用持续更新。在城市公交线路上的实验表明，与直接重新训练相比，DTCCL将整体规划性能提高了48.6％，验证了其在自动公共交通中可扩展的闭环策略改进的有效性。

## 🔬 方法详解

**问题定义**：自动驾驶巴士在实际运营中，由于环境的复杂性和动态性，经常出现需要人工干预的“脱离”事件。这些事件往往集中在特定的地理区域，并且是由于规划器在高度交互场景中失效导致的。传统的模仿学习方法难以有效利用这些稀疏的脱离数据，容易发生过拟合，导致策略改进效果不佳。因此，如何利用这些脱离事件来持续改进自动驾驶巴士的规划策略是一个关键问题。

**核心思路**：DTCCL的核心思路是利用脱离事件作为触发信号，通过数据增强生成对比学习所需的正负样本，并结合持续学习框架，在云端进行策略优化，然后将优化后的策略部署到边缘设备（自动驾驶巴士）上。通过这种云边协同的方式，实现自动驾驶巴士规划策略的持续改进。对比学习用于学习更好的策略表示，区分安全和不安全的行为。

**技术框架**：DTCCL框架主要包含以下几个模块：1) **脱离事件检测**：实时监测自动驾驶巴士的运行状态，当发生脱离事件时，触发数据增强流程。2) **云端数据增强**：基于脱离事件发生时的环境数据，通过扰动周围的智能体，生成正负样本。正样本模拟安全行为，负样本模拟不安全行为。3) **对比学习**：利用生成的数据，训练策略网络，使其能够更好地区分安全和不安全的行为。4) **持续学习**：将优化后的策略部署到自动驾驶巴士上，并在后续的运行过程中不断收集新的数据，重复上述流程，实现策略的持续改进。5) **云边协同**：云端负责数据增强和策略优化，边缘设备负责策略部署和数据收集。

**关键创新**：DTCCL的关键创新在于：1) **脱离触发的数据增强**：利用脱离事件作为触发信号，自动生成对比学习所需的正负样本，避免了人工标注的成本。2) **对比学习与持续学习的结合**：通过对比学习提升策略表示能力，并通过持续学习实现策略的持续改进。3) **云边协同的架构**：将计算密集型的数据增强和策略优化放在云端进行，减轻了边缘设备的计算负担。

**关键设计**：数据增强策略是关键设计之一，通过对周围车辆进行轨迹扰动，生成正负样本。正样本的扰动幅度较小，保证车辆的安全行驶；负样本的扰动幅度较大，模拟可能导致事故的危险行为。对比学习损失函数的设计也至关重要，目标是拉近正样本之间的距离，推远负样本之间的距离。网络结构方面，可以使用Transformer等模型来捕捉环境中的时序依赖关系。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18988v1/images/idea.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18988v1/images/framework2.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18988v1/images/platform.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，DTCCL框架在城市公交路线上取得了显著的性能提升。与直接重训练相比，DTCCL将整体规划性能提高了48.6%。这表明DTCCL能够有效利用脱离事件数据，提升自动驾驶巴士在复杂城市环境中的规划能力。此外，实验还验证了DTCCL框架的持续学习能力，即随着运行时间的增加，规划性能能够持续提升。

## 🎯 应用场景

DTCCL框架可应用于自动驾驶公交、物流车等固定线路的自动驾驶车辆，通过持续学习提升其在复杂城市环境中的规划能力。该研究有助于降低自动驾驶系统的部署和维护成本，提高其安全性和可靠性，加速自动驾驶技术的商业化落地。未来，该方法可以扩展到其他类型的自动驾驶车辆和更复杂的驾驶场景。

## 📄 摘要（原文）

> Autonomous buses run on fixed routes but must operate in open, dynamic urban environments. Disengagement events on these routes are often geographically concentrated and typically arise from planner failures in highly interactive regions. Such policy-level failures are difficult to correct using conventional imitation learning, which easily overfits to sparse disengagement data. To address this issue, this paper presents a Disengagement-Triggered Contrastive Continual Learning (DTCCL) framework that enables autonomous buses to improve planning policies through real-world operation. Each disengagement triggers cloud-based data augmentation that generates positive and negative samples by perturbing surrounding agents while preserving route context. Contrastive learning refines policy representations to better distinguish safe and unsafe behaviors, and continual updates are applied in a cloud-edge loop without human supervision. Experiments on urban bus routes demonstrate that DTCCL improves overall planning performance by 48.6 percent compared with direct retraining, validating its effectiveness for scalable, closed-loop policy improvement in autonomous public transport.

