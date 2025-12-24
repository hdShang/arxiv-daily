---
layout: default
title: "MMReview: A Multidisciplinary and Multimodal Benchmark for LLM-Based Peer Review Automation"
---

# MMReview: A Multidisciplinary and Multimodal Benchmark for LLM-Based Peer Review Automation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14146" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14146v4</a>
  <a href="https://arxiv.org/pdf/2508.14146.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14146v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14146v4', 'MMReview: A Multidisciplinary and Multimodal Benchmark for LLM-Based Peer Review Automation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xian Gao, Jiacheng Ruan, Zongyun Zhang, Jingsheng Gao, Ting Liu, Yuzhuo Fu

**分类**: cs.CL

**发布日期**: 2025-08-19 (更新: 2025-10-08)

**备注**: Work in progress

---

## 💡 一句话要点

**提出MMReview以解决学术同行评审自动化的评估标准缺失问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `同行评审` `大型语言模型` `多模态内容` `评估基准` `自动化系统` `跨学科研究` `人工智能`

## 📋 核心要点

1. 当前LLM在同行评审中的应用缺乏统一的评估标准，难以全面评估其生成评审的能力。
2. MMReview通过设计多模态内容和专家评论，提供了一个跨学科的综合评估基准，涵盖多种评审任务。
3. 实验结果表明，MMReview在评估LLMs和MLLMs的性能方面具有显著的有效性，推动了自动化评审系统的发展。

## 📝 摘要（中文）

随着学术出版物的快速增长，同行评审已成为研究社区中一项重要但耗时的责任。大型语言模型（LLMs）越来越多地被用于生成评审评论，但当前的LLM评审任务缺乏统一的评估基准，无法严格评估模型在生成全面、准确且符合人类偏好的评估方面的能力，尤其是在涉及图表等多模态内容的场景中。为了解决这一问题，我们提出了MMReview，这是一个涵盖多个学科和模态的综合基准。MMReview包含240篇论文的多模态内容和专家撰写的评审评论，涵盖人工智能、自然科学、工程科学和社会科学四个主要学科的17个研究领域。我们设计了13个任务，分为四个核心类别，旨在评估LLMs和多模态LLMs（MLLMs）在逐步生成评审、结果形成、人类偏好对齐和对抗输入操控的鲁棒性方面的表现。对16个开源模型和5个先进闭源模型进行的广泛实验展示了基准的全面性。我们希望MMReview成为建立自动化同行评审系统标准化基础的重要一步。

## 🔬 方法详解

**问题定义**：论文要解决的具体问题是现有LLM在同行评审中的应用缺乏统一的评估基准，导致无法有效评估其生成评审的全面性和准确性。现有方法在处理多模态内容（如图表）时表现不足。

**核心思路**：论文提出MMReview作为一个综合基准，涵盖多学科和多模态内容，设计了多项任务以评估LLMs和MLLMs的评审生成能力。通过引入专家撰写的评论，增强了评估的权威性和实用性。

**技术框架**：MMReview的整体架构包括四个核心类别的任务，共13个任务，分别评估逐步生成评审、结果形成、人类偏好对齐和对抗输入的鲁棒性。每个任务都针对特定的评估目标，确保全面性。

**关键创新**：MMReview的主要创新在于其跨学科和多模态的设计，填补了现有评估基准的空白，使得评估更加全面和准确。与现有方法相比，MMReview能够更好地处理复杂的多模态输入。

**关键设计**：在设计中，MMReview采用了专家撰写的评论作为基准，确保了评估的高标准。同时，任务设计考虑了不同学科的特点，确保了评估的适用性和有效性。

## 📊 实验亮点

实验结果显示，MMReview在评估LLMs和MLLMs的性能方面具有显著的有效性。通过对16个开源模型和5个闭源模型的测试，MMReview能够有效区分模型在生成评审时的表现，推动了自动化评审系统的标准化进程。

## 🎯 应用场景

该研究的潜在应用领域包括学术出版、科研评审和自动化评审系统的开发。MMReview为研究人员提供了一个标准化的评估工具，促进了同行评审的自动化进程，提升了评审的效率和质量，未来可能对学术界产生深远影响。

## 📄 摘要（原文）

> With the rapid growth of academic publications, peer review has become an essential yet time-consuming responsibility within the research community. Large Language Models (LLMs) have increasingly been adopted to assist in the generation of review comments; however, current LLM-based review tasks lack a unified evaluation benchmark to rigorously assess the models' ability to produce comprehensive, accurate, and human-aligned assessments, particularly in scenarios involving multimodal content such as figures and tables. To address this gap, we propose \textbf{MMReview}, a comprehensive benchmark that spans multiple disciplines and modalities. MMReview includes multimodal content and expert-written review comments for 240 papers across 17 research domains within four major academic disciplines: Artificial Intelligence, Natural Sciences, Engineering Sciences, and Social Sciences. We design a total of 13 tasks grouped into four core categories, aimed at evaluating the performance of LLMs and Multimodal LLMs (MLLMs) in step-wise review generation, outcome formulation, alignment with human preferences, and robustness to adversarial input manipulation. Extensive experiments conducted on 16 open-source models and 5 advanced closed-source models demonstrate the thoroughness of the benchmark. We envision MMReview as a critical step toward establishing a standardized foundation for the development of automated peer review systems.

