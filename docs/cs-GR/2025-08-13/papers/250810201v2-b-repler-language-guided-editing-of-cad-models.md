---
layout: default
title: "B-repLer: Language-guided Editing of CAD Models"
---

# B-repLer: Language-guided Editing of CAD Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10201" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10201v2</a>
  <a href="https://arxiv.org/pdf/2508.10201.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10201v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10201v2', 'B-repLer: Language-guided Editing of CAD Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yilin Liu, Niladri Shekhar Dutt, Changjian Li, Niloy J. Mitra

**分类**: cs.GR

**发布日期**: 2025-08-13 (更新: 2025-12-01)

**备注**: Project page: https://yilinliu77.github.io/brepler.github.io/

---

## 💡 一句话要点

**提出B-repLer以解决CAD模型语言引导编辑问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `CAD编辑` `自然语言处理` `多模态学习` `数据集生成` `语义连接`

## 📋 核心要点

1. 现有的语言引导CAD编辑方法缺乏用户命令与几何形状之间的语义连接，且依赖昂贵的构建历史。
2. B-repLer框架通过学习的潜在空间直接将自然语言与CAD模型编辑连接，避免了对构建历史的依赖。
3. 实验结果表明，B-repLer能够在高层次和模糊的输入下，准确执行复杂CAD形状的编辑，生成高质量输出。

## 📝 摘要（中文）

计算机辅助设计（CAD）模型因其紧凑性和精确性，成为工程物体设计和制造的行业标准。然而，语言引导的CAD编辑仍处于起步阶段，主要由于用户命令与底层形状几何之间缺乏语义连接，且缺乏配对的文本与编辑CAD数据集。尽管近期的多模态大语言模型（mLLMs）试图弥补这一差距，但其对CAD构建历史的依赖限制了其表达能力。本文提出了B-repLer，一个新颖的框架，通过在学习的潜在空间中直接将自然语言与CAD模型编辑连接，绕过了对构建历史的需求，能够对从简单棱柱部件到复杂B样条曲面定义的自由形状进行语义编辑。为此，我们引入了BrepEDIT-240K，这是首个大规模数据集，展示了如何利用现有CAD工具和mLLMs自动生成、验证和扩展所需的配对数据。我们的结果表明，B-repLer能够准确执行复杂CAD形状的编辑，甚至在输入编辑规范高层次且模糊的情况下，始终产生有效的高质量CAD输出。

## 🔬 方法详解

**问题定义**：本文旨在解决语言引导CAD编辑中用户命令与几何形状之间缺乏语义连接的问题。现有方法依赖于构建历史，这不仅昂贵且难以获取，限制了其适用性。

**核心思路**：B-repLer通过在学习的潜在空间中直接连接自然语言与CAD模型编辑，避免了对构建历史的依赖，从而实现对多种几何形状的语义编辑。

**技术框架**：该框架包括数据集生成、用户验证和模型训练三个主要模块。首先，利用现有CAD工具和mLLMs生成配对数据；其次，进行用户验证以确保数据质量；最后，训练模型以实现语言引导的CAD编辑。

**关键创新**：B-repLer的核心创新在于其能够在没有构建历史的情况下，直接通过自然语言进行CAD模型的编辑，这与现有方法的依赖性形成了鲜明对比。

**关键设计**：在模型设计中，采用了特定的损失函数以优化编辑效果，并通过调整网络结构来提高模型对复杂几何形状的适应能力。

## 📊 实验亮点

实验结果显示，B-repLer在复杂CAD形状的编辑任务中表现出色，能够处理高层次和模糊的输入规范，生成有效的高质量CAD输出。与传统方法相比，B-repLer在编辑准确性和输出质量上均有显著提升，展示了其在CAD编辑领域的强大潜力。

## 🎯 应用场景

B-repLer的研究成果在多个领域具有潜在应用价值，包括工程设计、产品原型制作和教育培训等。通过简化CAD模型的编辑过程，用户可以更高效地实现设计意图，降低了对专业知识的依赖，促进了设计的创新与灵活性。未来，该技术可能会推动CAD软件的智能化发展，使得设计过程更加人性化和高效。

## 📄 摘要（原文）

> Computer-Aided Design (CAD) models, given their compactness and precision, remain the industry standard for designing and fabricating engineering objects. However, language-guided CAD editing is still in its infancy, largely due to missing semantic connection between user commands and underlying shape geometry, a problem exacerbated by the shortage of paired text-and-edit CAD datasets. While recent Multimodal Large Language Models (mLLMs) have attempted to bridge this gap, their reliance on CAD construction history -- often an expensive and hard to obtain input -- severely limits their expressiveness and restricts their usage. We present B-repLer, a novel framework that directly connects natural language with editing CAD models by operating in a learned latent space. Importantly, our approach bypasses the need for construction history, enabling semantic edits on a wide range of geometries, from simple prismatic parts to complex freeform shapes defined by B-Spline surfaces. To facilitate this research, we introduce BrepEDIT-240K, the first large-scale dataset for this task. We demonstrate how this paired dataset can be automatically generated, (user) validated, and scaled by leveraging existing CAD tools, in conjunction with mLLMs, to create the required paired data without relying on any external annotations. Our results demonstrate that B-repLer can accurately perform complex edits on complex CAD shapes, even when the input edit specifications are high-level and ambiguous to interpret, consistently producing valid, high-quality CAD outputs enabling a class of text-guided edits not previously possible.

