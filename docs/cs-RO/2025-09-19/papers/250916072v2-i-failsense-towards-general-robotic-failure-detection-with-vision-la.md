---
layout: default
title: "I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models"
---

# I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16072" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16072v2</a>
  <a href="https://arxiv.org/pdf/2509.16072.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16072v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16072v2', 'I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Clemence Grislain, Hamed Rahimi, Olivier Sigaud, Mohamed Chetouani

**分类**: cs.RO

**发布日期**: 2025-09-19 (更新: 2025-09-22)

**🔗 代码/项目**: [PROJECT_PAGE](https://clemgris.github.io/I-FailSense/)

---

## 💡 一句话要点

**I-FailSense：利用视觉-语言模型实现通用机器人故障检测**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人故障检测` `视觉-语言模型` `语义错位` `集成学习` `语言条件操作`

## 📋 核心要点

1. 现有语言条件机器人操作方法在检测语义错位故障方面存在不足，难以保证真实环境中的稳健性。
2. I-FailSense通过后训练VLM，并集成连接到不同内部层的轻量级分类头（FS块）的预测，实现故障检测。
3. 实验表明，I-FailSense在语义错位检测方面优于现有VLM，并能泛化到其他故障类别和环境。

## 📝 摘要（中文）

在开放世界环境中，具备语言条件控制的机器人操作不仅需要精确的任务执行，还需要能够检测故障，以便在真实环境中稳健部署。尽管视觉-语言模型（VLM）的最新进展显著提高了机器人的空间推理和任务规划能力，但它们在识别自身故障方面的能力仍然有限。特别是一个关键但未被充分探索的挑战是检测语义错位错误，即机器人执行的任务在语义上是有意义的，但与给定的指令不一致。为了解决这个问题，我们提出了一种从现有的语言条件操作数据集中构建针对语义错位故障检测的数据集的方法。我们还提出了I-FailSense，一个具有基于grounding的仲裁功能的开源VLM框架，专门用于故障检测。我们的方法依赖于对基础VLM进行后训练，然后训练轻量级的分类头（称为FS块），这些分类头连接到VLM的不同内部层，并且它们的预测使用集成机制进行聚合。实验表明，I-FailSense在检测语义错位错误方面优于最先进的VLM，无论是在大小上可比的还是更大的VLM。值得注意的是，尽管仅在语义错位检测上进行训练，但I-FailSense可以推广到更广泛的机器人故障类别，并有效地转移到其他模拟环境和真实世界，具有零样本或最小的后训练。

## 🔬 方法详解

**问题定义**：论文旨在解决语言条件机器人操作中，机器人执行的任务在语义上合理但与指令不符的语义错位故障检测问题。现有方法难以有效识别此类故障，导致机器人操作的可靠性降低。

**核心思路**：论文的核心思路是利用视觉-语言模型（VLM）的语义理解能力，通过后训练和集成学习，使模型能够区分正确的任务执行和语义错位的故障。通过在VLM的不同层级添加轻量级的分类头，捕捉不同抽象层次的语义信息，并进行集成，提高故障检测的准确性和鲁棒性。

**技术框架**：I-FailSense框架包含以下主要步骤：1) 基于现有的语言条件操作数据集，构建专门针对语义错位故障检测的数据集。2) 对预训练的VLM进行后训练，使其适应故障检测任务。3) 在VLM的不同内部层添加轻量级的分类头（FS块）。4) 使用集成机制聚合来自不同FS块的预测结果，得到最终的故障检测结果。

**关键创新**：I-FailSense的关键创新在于：1) 提出了一种构建语义错位故障检测数据集的方法。2) 设计了一种基于VLM的故障检测框架，通过在不同层级添加分类头并进行集成，提高了故障检测的准确性和鲁棒性。3) 验证了该方法在零样本或少量样本情况下，向其他模拟环境和真实世界的泛化能力。

**关键设计**：FS块是轻量级的分类头，可以采用简单的全连接层或卷积神经网络。损失函数可以使用交叉熵损失或Focal Loss等。集成机制可以使用加权平均或投票等方法。具体的参数设置需要根据实际情况进行调整。

## 📊 实验亮点

I-FailSense在语义错位检测任务上显著优于现有VLM，包括大小可比和更大的模型。实验结果表明，该方法不仅在训练数据集上表现出色，而且能够泛化到其他模拟环境和真实世界，具有零样本或少量样本学习能力。这表明I-FailSense具有很强的实用性和泛化能力。

## 🎯 应用场景

I-FailSense可应用于各种语言条件机器人操作场景，例如家庭服务机器人、工业自动化机器人和医疗机器人等。该研究有助于提高机器人在复杂环境中的可靠性和安全性，减少人为干预，并促进机器人技术的广泛应用。未来，该方法可以扩展到其他类型的机器人故障检测，并与其他机器人控制算法相结合，实现更智能、更自主的机器人系统。

## 📄 摘要（原文）

> Language-conditioned robotic manipulation in open-world settings requires not only accurate task execution but also the ability to detect failures for robust deployment in real-world environments. Although recent advances in vision-language models (VLMs) have significantly improved the spatial reasoning and task-planning capabilities of robots, they remain limited in their ability to recognize their own failures. In particular, a critical yet underexplored challenge lies in detecting semantic misalignment errors, where the robot executes a task that is semantically meaningful but inconsistent with the given instruction. To address this, we propose a method for building datasets targeting Semantic Misalignment Failures detection, from existing language-conditioned manipulation datasets. We also present I-FailSense, an open-source VLM framework with grounded arbitration designed specifically for failure detection. Our approach relies on post-training a base VLM, followed by training lightweight classification heads, called FS blocks, attached to different internal layers of the VLM and whose predictions are aggregated using an ensembling mechanism. Experiments show that I-FailSense outperforms state-of-the-art VLMs, both comparable in size and larger, in detecting semantic misalignment errors. Notably, despite being trained only on semantic misalignment detection, I-FailSense generalizes to broader robotic failure categories and effectively transfers to other simulation environments and real-world with zero-shot or minimal post-training. The datasets and models are publicly released on HuggingFace (Webpage: https://clemgris.github.io/I-FailSense/).

