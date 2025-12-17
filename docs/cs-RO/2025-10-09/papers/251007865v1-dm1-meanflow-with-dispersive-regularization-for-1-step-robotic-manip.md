---
layout: default
title: DM1: MeanFlow with Dispersive Regularization for 1-Step Robotic Manipulation
---

# DM1: MeanFlow with Dispersive Regularization for 1-Step Robotic Manipulation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.07865" target="_blank" class="toolbar-btn">arXiv: 2510.07865v1</a>
    <a href="https://arxiv.org/pdf/2510.07865.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07865v1" 
            onclick="toggleFavorite(this, '2510.07865v1', 'DM1: MeanFlow with Dispersive Regularization for 1-Step Robotic Manipulation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Guowei Zou, Haitao Wang, Hejun Wu, Yukun Qian, Yuhang Wang, Weibing Li

**分类**: cs.RO, cs.AI

**发布日期**: 2025-10-09

**备注**: Website with code: https://guowei-zou.github.io/dm1/

---

## 💡 一句话要点

**DM1：通过分散正则化的MeanFlow实现单步机器人操作，解决表示崩溃问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人操作` `Flow模型` `分散正则化` `表示学习` `单步控制`

## 📋 核心要点

1. 现有基于Flow的机器人操作策略易发生表示崩溃，无法区分相似的视觉表征，导致精确操作任务失败。
2. DM1通过在MeanFlow中引入分散正则化，鼓励训练批次间的多样化表示，从而避免表示崩溃，同时保持单步推理效率。
3. 实验表明，DM1在推理速度上提升20-40倍，成功率提升10-20%，并在真实机器人上验证了其有效性。

## 📝 摘要（中文）

本文提出DM1（具有分散正则化的MeanFlow，用于单步机器人操作），这是一种新颖的Flow Matching框架，它将分散正则化集成到MeanFlow中，以防止表示崩溃，同时保持单步效率。DM1在不同的中间嵌入层采用多种分散正则化变体，鼓励跨训练批次的多样化表示，而无需引入额外的网络模块或专门的训练程序。在RoboMimic基准测试上的实验表明，DM1实现了20-40倍的更快推理速度（0.07秒 vs. 2-3.5秒），并将成功率提高了10-20个百分点，其中Lift任务的成功率达到99%，而基线为85%。在Franka Panda机器人上的真实机器人部署进一步验证了DM1可以有效地从模拟转移到物理世界。据我们所知，这是第一项利用表示正则化使基于Flow的策略在机器人操作中实现强大性能的工作，为高效而稳健的操作建立了一种简单而强大的方法。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人操作中，基于Flow的策略由于表示崩溃而导致的精确操作失败问题。现有方法难以区分相似的视觉表征，限制了策略的鲁棒性和泛化能力。

**核心思路**：论文的核心思路是在MeanFlow框架中引入分散正则化，通过鼓励训练批次间的多样化表示，防止表示崩溃。这种方法旨在提高模型对视觉输入的区分能力，从而提升操作的精确性和鲁棒性。

**技术框架**：DM1框架基于MeanFlow，并在其基础上添加了分散正则化模块。整体流程包括：1) 接收视觉输入；2) 通过MeanFlow生成动作分布；3) 在MeanFlow的中间嵌入层应用分散正则化；4) 输出最终的动作。该框架无需额外的网络模块或专门的训练程序。

**关键创新**：最关键的创新点在于将分散正则化应用于Flow-based的机器人操作策略中，以解决表示崩溃问题。与现有方法相比，DM1不需要复杂的网络结构或训练技巧，即可显著提升性能。

**关键设计**：DM1在不同的中间嵌入层采用多种分散正则化变体。具体的分散正则化方法（例如，最大均值差异MMD）和正则化强度需要根据具体任务进行调整。损失函数包括Flow Matching损失和分散正则化损失，通过调整两者的权重来平衡生成质量和表示多样性。

## 📊 实验亮点

DM1在RoboMimic基准测试中表现出色，推理速度提升20-40倍（0.07秒 vs. 2-3.5秒），成功率提升10-20%。在Lift任务中，DM1的成功率达到99%，而基线为85%。真实机器人实验也验证了DM1从模拟到物理世界的有效迁移。

## 🎯 应用场景

DM1具有广泛的应用前景，可应用于各种需要精确和鲁棒控制的机器人操作任务，例如装配、抓取、放置等。该方法可以提高机器人在复杂环境中的适应性和可靠性，降低操作失败的风险，并有望推动机器人技术在工业自动化、医疗保健等领域的应用。

## 📄 摘要（原文）

> The ability to learn multi-modal action distributions is indispensable for robotic manipulation policies to perform precise and robust control. Flow-based generative models have recently emerged as a promising solution to learning distributions of actions, offering one-step action generation and thus achieving much higher sampling efficiency compared to diffusion-based methods. However, existing flow-based policies suffer from representation collapse, the inability to distinguish similar visual representations, leading to failures in precise manipulation tasks. We propose DM1 (MeanFlow with Dispersive Regularization for One-Step Robotic Manipulation), a novel flow matching framework that integrates dispersive regularization into MeanFlow to prevent collapse while maintaining one-step efficiency. DM1 employs multiple dispersive regularization variants across different intermediate embedding layers, encouraging diverse representations across training batches without introducing additional network modules or specialized training procedures. Experiments on RoboMimic benchmarks show that DM1 achieves 20-40 times faster inference (0.07s vs. 2-3.5s) and improves success rates by 10-20 percentage points, with the Lift task reaching 99% success over 85% of the baseline. Real-robot deployment on a Franka Panda further validates that DM1 transfers effectively from simulation to the physical world. To the best of our knowledge, this is the first work to leverage representation regularization to enable flow-based policies to achieve strong performance in robotic manipulation, establishing a simple yet powerful approach for efficient and robust manipulation.

