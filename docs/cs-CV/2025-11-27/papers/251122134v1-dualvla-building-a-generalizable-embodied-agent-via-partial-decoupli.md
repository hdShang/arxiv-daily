---
layout: default
title: DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action
---

# DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22134" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22134v1</a>
  <a href="https://arxiv.org/pdf/2511.22134.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22134v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.22134v1', 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhen Fang, Zhuoyang Liu, Jiaming Liu, Hao Chen, Yu Zeng, Shiting Huang, Zehui Chen, Lin Chen, Shanghang Zhang, Feng Zhao

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-27

**🔗 代码/项目**: [PROJECT_PAGE](https://costaliya.github.io/DualVLA/)

---

## 💡 一句话要点

**DualVLA：通过解耦推理与动作，构建可泛化的具身智能体**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `具身智能` `视觉-语言-动作模型` `动作退化` `数据剪枝` `知识蒸馏` `多模态学习` `机器人操作`

## 📋 核心要点

1. 现有VLA模型在融合推理能力时，常出现动作性能下降的“动作退化”问题，限制了通用性。
2. DualVLA通过双层数据剪枝消除冗余推理，并采用双教师自适应蒸馏强化动作生成，保持推理能力。
3. DualVLA在SimplerEnv和多个多模态基准测试中表现出色，验证了其在动作执行和多模态理解上的平衡。

## 📝 摘要（中文）

为了构建具有强大推理能力的可泛化视觉-语言-动作（VLA）模型，一种常见策略是首先在机器人演示数据上训练一个专家VLA模型，以获得可靠的操作技能，然后结合混合标注的机器人数据和多模态数据，以恢复更广泛的推理能力。然而，我们观察到，与微调前的专家模型相比，由此产生的推理VLA模型通常会出现动作性能下降，我们称之为动作退化现象。为了解决这个问题，我们提出了DualVLA，它通过精心设计的后训练来增强动作性能，同时保持推理能力。我们首先引入了一种双层数据剪枝方法，该方法消除了冗余的具身推理，防止其对动作学习产生不利影响。为了进一步加强动作生成，我们设计了一种双教师自适应蒸馏策略，该策略为不同的数据域分配不同的监督信号，同时保持推理能力。为了填补通用VLA的评估空白，我们还提出了VLA Score，它将VLA能力解耦为推理、意图、动作和对齐维度，以便进行更细粒度的评估。实验表明，DualVLA在SimplerEnv中实现了61.0的平均成功率，并在八个竞争性多模态基准测试中实现了65.4的平均分数，表明在精确的动作执行和多模态理解之间取得了更强的平衡。

## 🔬 方法详解

**问题定义**：论文旨在解决通用视觉-语言-动作（VLA）模型在融合推理能力时出现的“动作退化”问题。现有方法通常先训练一个擅长动作的VLA模型，然后通过混合数据进行微调以提升推理能力，但微调后动作性能会显著下降，限制了模型的泛化能力。

**核心思路**：DualVLA的核心思路是在后训练阶段，通过解耦推理和动作的学习过程，在保持推理能力的同时，提升动作执行的精确性。具体来说，通过数据剪枝减少推理对动作学习的干扰，并通过自适应蒸馏强化动作生成。

**技术框架**：DualVLA包含以下主要模块：1) 预训练的VLA模型（专家模型）；2) 双层数据剪枝模块，用于去除冗余的具身推理数据；3) 双教师自适应蒸馏模块，利用专家模型和推理模型作为教师，指导学生模型学习；4) VLA Score评估指标，用于细粒度评估VLA模型的推理、意图、动作和对齐能力。

**关键创新**：DualVLA的关键创新在于：1) 提出了双层数据剪枝方法，有效减少了推理数据对动作学习的负面影响；2) 设计了双教师自适应蒸馏策略，能够根据数据域的不同，自适应地分配不同的监督信号，从而在保持推理能力的同时，提升动作执行的精度；3) 提出了VLA Score评估指标，为通用VLA模型的评估提供了一种更细粒度的方法。

**关键设计**：双层数据剪枝的具体实现未知，但其目标是去除对动作学习无益的推理数据。双教师自适应蒸馏策略中，如何确定不同数据域的监督信号分配比例是关键设计。VLA Score评估指标的具体计算方法未知，但其考虑了推理、意图、动作和对齐四个维度。

## 📊 实验亮点

DualVLA在SimplerEnv环境中取得了61.0%的平均成功率，相较于基线模型有显著提升。在八个竞争性多模态基准测试中，DualVLA获得了65.4的平均分数，表明其在多模态理解方面具有优势。这些实验结果验证了DualVLA在动作执行和多模态理解之间的平衡。

## 🎯 应用场景

DualVLA的研究成果可应用于机器人操作、自动驾驶、智能家居等领域。通过提升具身智能体的通用性和动作执行能力，可以使其更好地理解人类指令，完成复杂任务，并与环境进行更有效的交互。该研究有助于推动人机协作和智能自动化的发展。

## 📄 摘要（原文）

> To build a generalizable Vision-Language-Action (VLA) model with strong reasoning ability, a common strategy is to first train a specialist VLA on robot demonstrations to acquire reliable manipulation skills, and then incorporate mixed annotated robot data together with multimodal data to restore broader reasoning capabilities. However, we observe that the resulting reasoning VLA often suffers from degraded action performance compared to the specialist model before fine-tuning, a phenomenon we refer to as action degeneration. To address this issue, we propose DualVLA, which enhances action performance through carefully designed post-training while still preserving reasoning capability. We first introduce a dual-layer data pruning method that removes redundant embodied reasoning, preventing it from adversely influencing action learning. To further strengthen action generation, we design a dual-teacher adaptive distillation strategy that assigns different supervision signals to different data domains while maintaining reasoning ability. To fill the evaluation gap for generalist VLAs, we also propose VLA Score, which decouples VLA capability into reasoning, intention, action, and alignment dimensions for a more fine-grained assessment. Experiments show that DualVLA achieves an average success rate of 61.0 in SimplerEnv and an average score of 65.4 across eight competitive multimodal benchmarks, demonstrating a stronger balance between precise action execution and multimodal understanding. Project Website: https://costaliya.github.io/DualVLA/.

