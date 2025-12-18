---
layout: default
title: VITA-VLA: Efficiently Teaching Vision-Language Models to Act via Action Expert Distillation
---

# VITA-VLA: Efficiently Teaching Vision-Language Models to Act via Action Expert Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09607" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09607v2</a>
  <a href="https://arxiv.org/pdf/2510.09607.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09607v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.09607v2', 'VITA-VLA: Efficiently Teaching Vision-Language Models to Act via Action Expert Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaoqi Dong, Chaoyou Fu, Haihan Gao, Yi-Fan Zhang, Chi Yan, Chu Wu, Xiaoyu Liu, Yunhang Shen, Jing Huo, Deqiang Jiang, Haoyu Cao, Yang Gao, Xing Sun, Ran He, Caifeng Shan

**分类**: cs.CV

**发布日期**: 2025-10-10 (更新: 2025-10-17)

**备注**: Homepage: https://ltbai.github.io/VITA-VLA/

---

## 💡 一句话要点

**提出VITA-VLA，通过动作专家蒸馏高效训练视觉-语言模型以执行机器人动作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `知识蒸馏` `机器人操作` `预训练模型` `多模态学习`

## 📋 核心要点

1. 现有视觉-语言-动作(VLA)模型训练成本高昂，难以充分利用预训练视觉-语言模型(VLM)的强大感知能力。
2. VITA-VLA通过知识蒸馏，将预训练的小型动作模型的知识迁移到VLM，使其具备动作执行能力，避免从头训练。
3. 实验表明，VITA-VLA在多个机器人操作任务上显著优于现有方法，并降低了训练成本，提升了效率。

## 📝 摘要（中文）

本文提出了一种基于蒸馏的框架，旨在通过迁移预训练的小型动作模型的知识，使视觉-语言模型(VLM)具备动作执行能力。该架构保留了原始VLM的结构，仅添加了一个动作token和一个状态编码器来整合物理输入。采用两阶段训练策略：首先，通过将VLM隐藏状态映射到小型动作模型的动作空间进行轻量级对齐，从而有效重用其预训练的动作解码器，避免昂贵的预训练。其次，选择性地微调语言模型、状态编码器和动作模块，使系统能够整合多模态输入并生成精确的动作。动作token为VLM提供了一个直接预测未来动作的句柄，而状态编码器允许模型整合视觉之外的机器人动力学信息。实验表明，该方法在LIBERO和LIBERO-LONG上分别取得了97.3%和93.5%的平均成功率，并在真实世界的操作任务中优于教师模型，证明了动作蒸馏能够有效生成精确动作，同时显著降低训练成本。

## 🔬 方法详解

**问题定义**：现有VLA模型通常需要从头开始训练，计算成本高昂，且难以充分利用预训练VLMs强大的视觉和语言理解能力。这些模型在泛化性和效率方面存在瓶颈，尤其是在复杂的操作任务中。

**核心思路**：VITA-VLA的核心思路是通过知识蒸馏，将预训练的小型动作模型的知识迁移到大型VLM中，从而使VLM具备动作执行能力。这种方法避免了从头训练大型VLA模型的需要，显著降低了计算成本，并能有效利用VLMs的预训练知识。

**技术框架**：VITA-VLA的整体架构包括一个预训练的VLM、一个动作token、一个状态编码器和一个预训练的小型动作模型（作为教师模型）。训练过程分为两个阶段：1) 轻量级对齐：将VLM的隐藏状态映射到小型动作模型的动作空间，以便重用其预训练的动作解码器。2) 选择性微调：微调语言模型、状态编码器和动作模块，以整合多模态输入并生成精确的动作。

**关键创新**：VITA-VLA的关键创新在于其基于蒸馏的训练框架，该框架能够有效地将动作知识从小型动作模型迁移到大型VLM。通过引入动作token和状态编码器，VITA-VLA能够更好地整合视觉、语言和机器人状态信息，从而生成更精确的动作。与从头训练相比，这种方法显著提高了训练效率。

**关键设计**：动作token被添加到VLM中，作为预测未来动作的直接句柄。状态编码器用于编码机器人状态信息，例如关节角度和速度，这些信息可能无法仅从视觉输入中获得。损失函数包括动作预测损失和状态预测损失，用于指导模型的训练。选择性微调策略用于避免过度拟合，并保持VLM的泛化能力。

## 📊 实验亮点

VITA-VLA在LIBERO数据集上取得了97.3%的平均成功率，相比之前的最佳方法提升了11.8%。在更具挑战性的LIBERO-LONG数据集上，成功率达到了93.5%，提升幅度高达24.5%。在真实世界的机器人操作实验中，VITA-VLA的成功率为82.0%，比教师模型提高了17%。这些结果表明，VITA-VLA能够有效地将动作知识迁移到VLM，并显著提高机器人的操作性能。

## 🎯 应用场景

VITA-VLA可应用于各种机器人操作任务，例如物体抓取、装配、导航等。该方法能够降低机器人学习的成本，提高机器人的智能化水平，并促进机器人在工业自动化、医疗保健、家庭服务等领域的广泛应用。未来，该技术有望应用于更复杂的机器人任务，例如人机协作和自主决策。

## 📄 摘要（原文）

> Vision-Language Action (VLA) models significantly advance robotic manipulation by leveraging the strong perception capabilities of pretrained vision-language models (VLMs). By integrating action modules into these pretrained models, VLA methods exhibit improved generalization. However, training them from scratch is costly. In this work, we propose a simple yet effective distillation-based framework that equips VLMs with action-execution capability by transferring knowledge from pretrained small action models. Our architecture retains the original VLM structure, adding only an action token and a state encoder to incorporate physical inputs. To distill action knowledge, we adopt a two-stage training strategy. First, we perform lightweight alignment by mapping VLM hidden states into the action space of the small action model, enabling effective reuse of its pretrained action decoder and avoiding expensive pretraining. Second, we selectively fine-tune the language model, state encoder, and action modules, enabling the system to integrate multimodal inputs with precise action generation. Specifically, the action token provides the VLM with a direct handle for predicting future actions, while the state encoder allows the model to incorporate robot dynamics not captured by vision alone. This design yields substantial efficiency gains over training large VLA models from scratch. Compared with previous state-of-the-art methods, our method achieves 97.3% average success rate on LIBERO (11.8% improvement) and 93.5% on LIBERO-LONG (24.5% improvement). In real-world experiments across five manipulation tasks, our method consistently outperforms the teacher model, achieving 82.0% success rate (17% improvement), which demonstrate that action distillation effectively enables VLMs to generate precise actions while substantially reducing training costs.

