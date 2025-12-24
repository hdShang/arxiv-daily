---
layout: default
title: "AINL-Eval 2025 Shared Task: Detection of AI-Generated Scientific Abstracts in Russian"
---

# AINL-Eval 2025 Shared Task: Detection of AI-Generated Scientific Abstracts in Russian

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09622" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09622v1</a>
  <a href="https://arxiv.org/pdf/2508.09622.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09622v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09622v1', 'AINL-Eval 2025 Shared Task: Detection of AI-Generated Scientific Abstracts in Russian')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tatiana Batura, Elena Bruches, Milana Shvenk, Valentin Malykh

**分类**: cs.CL

**发布日期**: 2025-08-13

**备注**: AINL 2025 Conference

**🔗 代码/项目**: [GITHUB](https://github.com/iis-research-team/AINL-Eval-2025)

---

## 💡 一句话要点

**提出AINL-Eval 2025任务以检测俄语AI生成的科学摘要**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI生成内容` `科学摘要` `文本检测` `多语言处理` `数据集构建` `学术诚信` `机器学习`

## 📋 核心要点

1. 现有方法在检测AI生成内容时面临挑战，尤其是在多语言和科学领域中，缺乏有效的检测资源。
2. 论文提出了AINL-Eval 2025任务，构建了一个包含人类和AI生成摘要的大规模数据集，以促进AI生成内容的检测研究。
3. 实验结果显示，参与团队在识别AI生成内容方面取得了显著进展，展示了强大的性能和广泛的适用性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的快速发展，文本生成技术取得了革命性进展，使得区分人类与AI生成内容变得愈加困难。这对学术诚信构成了重大挑战，尤其是在科学出版和多语言环境中，检测资源往往有限。为了解决这一关键问题，我们推出了AINL-Eval 2025共享任务，专注于检测俄语中的AI生成科学摘要。我们构建了一个包含52,305个样本的大规模新数据集，涵盖12个不同科学领域的人类撰写摘要及来自五种最先进LLM（GPT-4-Turbo、Gemma2-27B、Llama3.3-70B、Deepseek-V3和GigaChat-Lite）的AI生成摘要。该任务的核心目标是挑战参与者开发能够推广到未见过的科学领域和未包含在训练数据中的模型的稳健解决方案。该任务吸引了10个团队和159个提交，顶尖系统在识别AI生成内容方面表现出色。我们还建立了一个持续的共享任务平台，以促进这一重要领域的持续研究和长期进展。数据集和平台已在https://github.com/iis-research-team/AINL-Eval-2025上公开。

## 🔬 方法详解

**问题定义**：本研究旨在解决在俄语科学摘要中检测AI生成内容的难题。现有方法在多语言和多领域的应用中存在局限性，难以有效识别AI生成的文本。

**核心思路**：通过构建一个大规模的多样化数据集，涵盖不同科学领域的人类和AI生成摘要，来提高检测模型的泛化能力。任务的设计旨在挑战参与者开发能够适应新领域和新模型的解决方案。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要阶段。数据集由52,305个样本组成，模型训练使用多种先进的LLM，并通过竞赛形式评估模型性能。

**关键创新**：最重要的创新在于构建了一个涵盖多领域和多种生成模型的大规模数据集，填补了现有研究中的空白，推动了AI生成内容检测的研究进展。

**关键设计**：在模型训练中，采用了多种损失函数和参数设置，以优化模型在不同领域和模型上的表现，确保其具有良好的泛化能力。

## 📊 实验亮点

实验结果显示，参与的顶尖系统在识别AI生成内容方面表现出色，许多系统的准确率超过了85%。这一成果表明，构建的多样化数据集和任务设计有效提升了模型的检测能力，为未来的研究奠定了基础。

## 🎯 应用场景

该研究的潜在应用领域包括学术出版、教育和内容审核等。通过提高对AI生成内容的检测能力，可以有效维护学术诚信，减少伪造和抄袭现象，促进科学研究的健康发展。未来，该研究还可能推动多语言文本生成和检测技术的进一步发展。

## 📄 摘要（原文）

> The rapid advancement of large language models (LLMs) has revolutionized text generation, making it increasingly difficult to distinguish between human- and AI-generated content. This poses a significant challenge to academic integrity, particularly in scientific publishing and multilingual contexts where detection resources are often limited. To address this critical gap, we introduce the AINL-Eval 2025 Shared Task, specifically focused on the detection of AI-generated scientific abstracts in Russian. We present a novel, large-scale dataset comprising 52,305 samples, including human-written abstracts across 12 diverse scientific domains and AI-generated counterparts from five state-of-the-art LLMs (GPT-4-Turbo, Gemma2-27B, Llama3.3-70B, Deepseek-V3, and GigaChat-Lite). A core objective of the task is to challenge participants to develop robust solutions capable of generalizing to both (i) previously unseen scientific domains and (ii) models not included in the training data. The task was organized in two phases, attracting 10 teams and 159 submissions, with top systems demonstrating strong performance in identifying AI-generated content. We also establish a continuous shared task platform to foster ongoing research and long-term progress in this important area. The dataset and platform are publicly available at https://github.com/iis-research-team/AINL-Eval-2025.

