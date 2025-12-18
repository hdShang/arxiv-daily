---
layout: default
title: EvoCAD: Evolutionary CAD Code Generation with Vision Language Models
---

# EvoCAD: Evolutionary CAD Code Generation with Vision Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11631" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11631v1</a>
  <a href="https://arxiv.org/pdf/2510.11631.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11631v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.11631v1', 'EvoCAD: Evolutionary CAD Code Generation with Vision Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tobias Preintner, Weixuan Yuan, Adrian König, Thomas Bäck, Elena Raponi, Niki van Stein

**分类**: cs.CV, cs.AI, cs.NE

**发布日期**: 2025-10-13

**备注**: Accepted to IEEE ICTAI 2025

---

## 💡 一句话要点

**EvoCAD：利用视觉语言模型与进化算法生成CAD代码**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `CAD模型生成` `视觉语言模型` `进化算法` `拓扑结构评估` `3D对象` `符号表示` `GPT-4V` `GPT-4o`

## 📋 核心要点

1. 现有CAD对象生成方法在拓扑结构正确性方面存在不足，难以保证生成对象的语义合理性。
2. EvoCAD结合视觉语言模型和进化算法，通过迭代优化CAD对象的符号表示，提升生成质量。
3. 实验表明，EvoCAD在CADPrompt数据集上优于现有方法，尤其在拓扑结构正确性方面表现突出。

## 📝 摘要（中文）

本文提出EvoCAD，一种结合视觉语言模型和进化计算算法，通过符号表示生成计算机辅助设计(CAD)对象的方法。该方法首先采样多个CAD对象，然后利用视觉语言和推理语言模型，通过进化算法进行优化。使用GPT-4V和GPT-4o在CADPrompt基准数据集上评估EvoCAD，并与现有方法进行比较。此外，本文还引入了两个基于欧拉特征定义的拓扑属性的新指标，用于捕捉3D对象之间的语义相似性。实验结果表明，EvoCAD在多个指标上优于现有方法，尤其是在生成拓扑结构正确的对象方面，并且可以通过我们提出的两个新指标进行有效评估，从而补充现有的空间指标。

## 🔬 方法详解

**问题定义**：现有CAD对象生成方法难以保证生成对象的拓扑结构正确性，导致生成的3D模型可能在语义上不合理，例如出现不连通或孔洞等问题。此外，缺乏有效的拓扑结构评估指标，难以准确衡量生成模型的质量。

**核心思路**：EvoCAD的核心思路是利用大型语言模型（LLM）的生成能力和进化算法的优化能力，通过迭代改进CAD对象的符号表示，使其在视觉和语义上更符合目标。通过进化算法，选择和变异CAD对象，并使用视觉语言模型评估其质量，从而逐步优化生成结果。

**技术框架**：EvoCAD的整体框架包括以下几个主要阶段：1) 初始化：随机生成多个CAD对象的符号表示。2) 评估：使用视觉语言模型（如GPT-4V或GPT-4o）评估每个CAD对象的质量，并结合推理语言模型进行进一步的语义评估。3) 选择：根据评估结果，选择表现最好的CAD对象作为父代。4) 变异：对父代CAD对象的符号表示进行变异，生成新的CAD对象。5) 迭代：重复评估、选择和变异过程，直到达到预定的迭代次数或满足收敛条件。

**关键创新**：EvoCAD的关键创新在于：1) 结合了视觉语言模型和进化算法，实现了CAD对象的迭代优化。2) 提出了基于欧拉特征的拓扑结构评估指标，能够有效衡量生成对象的拓扑正确性。3) 利用视觉语言模型进行CAD对象的质量评估，能够捕捉更丰富的语义信息。

**关键设计**：EvoCAD的关键设计包括：1) 使用符号表示来描述CAD对象，便于语言模型处理和进化算法操作。2) 使用GPT-4V或GPT-4o等视觉语言模型进行CAD对象的视觉质量评估，并结合推理语言模型进行语义一致性检查。3) 定义了基于欧拉特征的拓扑结构评估指标，包括连通分量数和孔洞数，用于衡量生成对象的拓扑正确性。4) 进化算法采用选择、交叉和变异等操作，以优化CAD对象的符号表示。

## 📊 实验亮点

EvoCAD在CADPrompt数据集上取得了显著的性能提升，尤其是在拓扑结构正确性方面。实验结果表明，EvoCAD在多个指标上优于现有方法，并且通过提出的基于欧拉特征的新指标，能够更有效地评估生成模型的拓扑质量。例如，EvoCAD在生成拓扑结构正确的对象方面，相比于基线方法提升了XX%（具体数据未知）。

## 🎯 应用场景

EvoCAD可应用于自动化CAD模型设计、定制化产品生成、游戏资产创建等领域。通过结合自然语言描述和视觉信息，EvoCAD能够帮助用户快速生成满足特定需求的3D模型，降低设计门槛，提高设计效率。未来，EvoCAD有望与虚拟现实、增强现实等技术结合，实现更加智能和交互式的设计体验。

## 📄 摘要（原文）

> Combining large language models with evolutionary computation algorithms represents a promising research direction leveraging the remarkable generative and in-context learning capabilities of LLMs with the strengths of evolutionary algorithms. In this work, we present EvoCAD, a method for generating computer-aided design (CAD) objects through their symbolic representations using vision language models and evolutionary optimization. Our method samples multiple CAD objects, which are then optimized using an evolutionary approach with vision language and reasoning language models. We assess our method using GPT-4V and GPT-4o, evaluating it on the CADPrompt benchmark dataset and comparing it to prior methods. Additionally, we introduce two new metrics based on topological properties defined by the Euler characteristic, which capture a form of semantic similarity between 3D objects. Our results demonstrate that EvoCAD outperforms previous approaches on multiple metrics, particularly in generating topologically correct objects, which can be efficiently evaluated using our two novel metrics that complement existing spatial metrics.

