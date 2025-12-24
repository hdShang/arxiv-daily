---
layout: default
title: "ExT: Towards Scalable Autonomous Excavation via Large-Scale Multi-Task Pretraining and Fine-Tuning"
---

# ExT: Towards Scalable Autonomous Excavation via Large-Scale Multi-Task Pretraining and Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14992" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14992v2</a>
  <a href="https://arxiv.org/pdf/2509.14992.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14992v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14992v2', 'ExT: Towards Scalable Autonomous Excavation via Large-Scale Multi-Task Pretraining and Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Zhai, Lorenzo Terenzi, Patrick Frey, Diego Garcia Soto, Pascal Egli, Marco Hutter

**分类**: cs.RO

**发布日期**: 2025-09-18 (更新: 2025-09-22)

---

## 💡 一句话要点

**ExT：基于大规模多任务预训练和微调实现可扩展的自主挖掘**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自主挖掘` `多任务学习` `预训练` `微调` `强化学习` `机器人` `重型机械`

## 📋 核心要点

1. 现有自主挖掘系统依赖于高度工程化的任务特定控制器，难以适应新的工作环境和硬件配置。
2. ExT框架通过大规模多任务预训练和微调，使挖掘策略能够泛化到新的任务和操作条件。
3. 实验表明，ExT策略在仿真和真实世界中均能达到厘米级精度，并能快速适应新的任务和机器配置。

## 📝 摘要（中文）

本文提出了ExT，一个统一的开源框架，用于大规模演示数据收集、多任务挖掘策略的预训练和微调。ExT策略首先基于从多种专家收集的大规模演示数据进行训练，然后通过监督微调（SFT）或强化学习微调（RLFT）进行微调，以适应新的任务或操作条件。通过仿真和真实世界的实验，证明了预训练的ExT策略能够以厘米级的精度执行完整的挖掘周期，并成功地从仿真转移到真实机器，性能与专门的单任务控制器相当。此外，在仿真中，证明了ExT的微调流程能够快速适应新的任务、分布外条件和机器配置，同时保持在先前学习任务上的强大性能。这些结果突出了ExT作为可扩展和通用自主挖掘基础的潜力。

## 🔬 方法详解

**问题定义**：自主挖掘面临的挑战在于如何使挖掘机能够适应各种不同的工作环境、任务需求和硬件配置。现有的方法通常依赖于针对特定任务设计的控制器，需要大量的人工调整，难以扩展到新的场景。因此，需要一种能够泛化到不同任务和环境的自主挖掘策略。

**核心思路**：本文的核心思路是利用大规模多任务预训练和微调的方法，学习一个通用的挖掘策略。通过在大量不同任务和环境的数据上进行预训练，使模型能够学习到挖掘任务的基本规律和通用技能。然后，通过微调，使模型能够快速适应新的任务和环境。这种方法类似于自然语言处理中的预训练语言模型，可以显著提高模型的泛化能力和学习效率。

**技术框架**：ExT框架包含三个主要阶段：数据收集、预训练和微调。首先，收集来自不同专家的大规模演示数据，包括仿真数据和真实数据。然后，使用这些数据对挖掘策略进行预训练，使其学习到挖掘任务的基本技能。最后，根据具体的任务和环境，使用监督微调（SFT）或强化学习微调（RLFT）对预训练模型进行微调，使其能够适应新的场景。

**关键创新**：ExT的关键创新在于将大规模多任务预训练和微调的方法应用于自主挖掘领域。与传统的任务特定控制器相比，ExT策略具有更强的泛化能力和适应性，能够快速适应新的任务和环境。此外，ExT框架还提供了一个统一的开源平台，方便研究人员进行数据收集、模型训练和实验验证。

**关键设计**：ExT框架使用Transformer网络作为挖掘策略的模型结构。预训练阶段使用行为克隆损失函数，使模型学习模仿专家的行为。微调阶段可以使用监督微调或强化学习微调。监督微调使用交叉熵损失函数，强化学习微调使用PPO算法。为了提高模型的泛化能力，ExT框架还使用了数据增强和领域随机化等技术。

## 📊 实验亮点

实验结果表明，预训练的ExT策略能够以厘米级的精度执行完整的挖掘周期，并成功地从仿真转移到真实机器，性能与专门的单任务控制器相当。在仿真中，ExT的微调流程能够快速适应新的任务、分布外条件和机器配置，同时保持在先前学习任务上的强大性能。例如，在适应新的机器配置时，ExT仅需少量数据即可达到与专门控制器相当的性能。

## 🎯 应用场景

ExT框架具有广泛的应用前景，可用于各种自主挖掘任务，例如建筑工地、矿山开采、灾害救援等。通过ExT，可以显著提高挖掘机的自动化程度和工作效率，降低人工成本和安全风险。此外，ExT还可以应用于其他类型的重型机械，例如推土机、装载机等，实现更广泛的自动化。

## 📄 摘要（原文）

> Scaling up the deployment of autonomous excavators is of great economic and societal importance. Yet it remains a challenging problem, as effective systems must robustly handle unseen worksite conditions and new hardware configurations. Current state-of-the-art approaches rely on highly engineered, task-specific controllers, which require extensive manual tuning for each new scenario. In contrast, recent advances in large-scale pretrained models have shown remarkable adaptability across tasks and embodiments in domains such as manipulation and navigation, but their applicability to heavy construction machinery remains largely unexplored. In this work, we introduce ExT, a unified open-source framework for large-scale demonstration collection, pretraining, and fine-tuning of multitask excavation policies. ExT policies are first trained on large-scale demonstrations collected from a mix of experts, then fine-tuned either with supervised fine-tuning (SFT) or reinforcement learning fine-tuning (RLFT) to specialize to new tasks or operating conditions. Through both simulation and real-world experiments, we show that pretrained ExT policies can execute complete excavation cycles with centimeter-level accuracy, successfully transferring from simulation to real machine with performance comparable to specialized single-task controllers. Furthermore, in simulation, we demonstrate that ExT's fine-tuning pipelines allow rapid adaptation to new tasks, out-of-distribution conditions, and machine configurations, while maintaining strong performance on previously learned tasks. These results highlight the potential of ExT to serve as a foundation for scalable and generalizable autonomous excavation.

