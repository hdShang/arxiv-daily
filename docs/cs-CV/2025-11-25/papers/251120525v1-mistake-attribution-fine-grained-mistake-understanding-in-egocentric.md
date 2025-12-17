---
layout: default
title: Mistake Attribution: Fine-Grained Mistake Understanding in Egocentric Videos
---

# Mistake Attribution: Fine-Grained Mistake Understanding in Egocentric Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.20525" class="toolbar-btn" target="_blank">📄 arXiv: 2511.20525v1</a>
  <a href="https://arxiv.org/pdf/2511.20525.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20525v1" onclick="toggleFavorite(this, '2511.20525v1', 'Mistake Attribution: Fine-Grained Mistake Understanding in Egocentric Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yayuan Li, Aadit Jain, Filippos Bellos, Jason J. Corso

**分类**: cs.CV

**发布日期**: 2025-11-25

**备注**: 11 pages, 4 figures, 6 tables

---

## 💡 一句话要点

**提出Mistake Attribution (MATT)任务，用于细粒度理解以自我为中心的视频中的人类错误。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `错误归因` `以自我为中心视频` `细粒度理解` `视频语言模型` `注意力机制`

## 📋 核心要点

1. 现有错误理解工作缺乏细粒度输出，无法具体定位错误原因和发生位置。
2. 提出Mistake Attribution任务，将错误归因于指令文本的语义角色、不可逆转的时间点和空间位置。
3. 构建MisEngine数据引擎，生成大规模错误数据集，并提出MisFormer模型，在多个基准测试中表现优异。

## 📝 摘要（中文）

本文提出了Mistake Attribution (MATT)任务，旨在对以自我为中心的视频中人类的错误进行细粒度理解。与以往缺乏细粒度输出的错误理解工作不同，MATT将错误具体地归因于输入的指令文本或尝试视频。MATT确定违反了指令的哪个部分（语义角色），偏差变得不可逆转的时间点（Point-of-No-Return, PNR），以及错误出现在PNR帧中的位置。我们开发了MisEngine，一个数据引擎，可以从现有数据集中自动构建具有丰富归因信息的错误样本，并继承它们的注释。应用于大型以自我为中心的语料库，MisEngine产生了EPIC-KITCHENS-M和Ego4D-M两个数据集，它们比以往的错误数据集大两个数量级。然后，我们提出了MisFormer，一个统一的基于注意力的模型，用于跨语义（什么）、时间（何时）和空间（何地）维度进行错误归因，并使用MisEngine监督进行训练。在我们新的数据集和先前的基准测试上的实验表明，MisFormer优于强大的视频-语言、时间定位、手-对象交互和错误检测基线。

## 🔬 方法详解

**问题定义**：论文旨在解决以自我为中心的视频中人类错误理解的细粒度问题。现有方法通常只能检测错误，而无法提供错误的具体原因、发生时间以及发生位置等信息。这限制了对人类行为的深入理解和智能助手的有效干预。

**核心思路**：论文的核心思路是将错误归因分解为三个维度：语义（指令的哪个部分被违反）、时间（偏差变得不可逆转的时间点）和空间（错误发生的具体位置）。通过对这三个维度进行建模，可以实现对错误的细粒度理解。

**技术框架**：整体框架包含两个主要部分：MisEngine数据引擎和MisFormer模型。MisEngine负责从现有数据集中自动构建具有丰富归因信息的错误样本。MisFormer是一个统一的基于注意力的模型，用于跨语义、时间和空间维度进行错误归因。该模型接收视频和指令文本作为输入，输出错误发生的语义角色、Point-of-No-Return (PNR)以及PNR帧中的错误位置。

**关键创新**：论文的关键创新在于提出了Mistake Attribution (MATT)任务，并设计了MisEngine数据引擎和MisFormer模型来解决该任务。MATT任务定义了错误归因的三个维度，为细粒度错误理解提供了明确的目标。MisEngine能够自动生成大规模的错误数据集，解决了数据稀缺的问题。MisFormer模型则通过统一的注意力机制，实现了跨多个维度的错误归因。

**关键设计**：MisFormer模型采用Transformer架构，使用多头注意力机制来建模视频和文本之间的关系。模型包含三个输出分支，分别预测语义角色、PNR和错误位置。PNR的预测采用时间定位的方法，使用分类器预测每个帧是否为PNR。错误位置的预测采用目标检测的方法，使用边界框回归来定位错误在PNR帧中的位置。损失函数包括语义角色分类损失、PNR时间定位损失和错误位置检测损失。

## 📊 实验亮点

论文提出了EPIC-KITCHENS-M和Ego4D-M两个大规模错误数据集，比以往数据集大两个数量级。MisFormer模型在这些数据集以及先前的基准测试中均取得了显著的性能提升，超越了现有的视频-语言、时间定位、手-对象交互和错误检测基线。

## 🎯 应用场景

该研究成果可应用于智能助手、机器人辅助教学、人机交互等领域。通过理解人类在操作过程中的错误，智能系统可以提供更精准的指导和帮助，提高操作效率和安全性。例如，在烹饪教学中，系统可以识别用户在哪个步骤出错，并给出相应的纠正建议。

## 📄 摘要（原文）

> We introduce Mistake Attribution (MATT), a task for fine-grained understanding of human mistakes in egocentric video. Unlike prior mistake understanding work, which lacks fine-grained output, MATT concretely attributes mistakes to the input instruction text or the attempt video. MATT determines what part of the instruction is violated (semantic role), when the deviation becomes irreversible (the Point-of-No-Return, PNR), and where the mistake appears in the PNR frame. We develop MisEngine, a data engine that automatically constructs attribution-rich mistake samples from existing datasets and inherits their annotations. Applied to large egocentric corpora, MisEngine yields EPIC-KITCHENS-M and Ego4D-M, two datasets that are up to two orders of magnitude larger than prior mistake datasets. We then present MisFormer, a unified attention-based model for mistake attribution across semantic (what), temporal (when), and spatial (where) dimensions, trained using MisEngine supervision. Experiments on our new datasets and prior benchmarks show that MisFormer outperforms strong video-language, temporal localization, hand-object interaction, and mistake-detection baselines.

