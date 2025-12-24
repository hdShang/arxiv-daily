---
layout: default
title: Bye-bye, Bluebook? Automating Legal Procedure with Large Language Models
---

# Bye-bye, Bluebook? Automating Legal Procedure with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02763" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02763v1</a>
  <a href="https://arxiv.org/pdf/2505.02763.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02763v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02763v1', 'Bye-bye, Bluebook? Automating Legal Procedure with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Matthew Dahl

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2025-05-05

---

## 💡 一句话要点

**利用大型语言模型自动化法律程序以应对复杂引用规则**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法律自动化` `大型语言模型` `引用规则` `蓝皮书` `合规性评估` `上下文学习` `法律技术` `数据集构建`

## 📋 核心要点

1. 核心问题：现有大型语言模型在遵循复杂法律引用规则方面的准确性不足，导致法律实践中的合规性风险。
2. 方法要点：构建866个蓝皮书任务的数据集，评估多种大型语言模型在生成法律引用时的表现。
3. 实验或效果：模型生成合规引用的准确率仅为69%-74%，即使经过上下文学习，准确率也仅提升至77%。

## 📝 摘要（中文）

法律实践要求严格遵循程序规则，而美国的《蓝皮书：统一引用系统》是其中最复杂的之一。本文构建了一个包含866个蓝皮书任务的原始数据集，测试了OpenAI、Anthropic、Google、Meta和DeepSeek的旗舰大型语言模型（LLMs）。研究结果表明，这些模型仅在69%-74%的情况下生成完全合规的蓝皮书引用，而通过上下文学习蓝皮书的基本规则，准确率仅提高至77%。这些结果警示我们在法律领域自动化时，不能仅依赖现成的LLMs，尤其是在程序遵循至关重要的情况下。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成法律引用时的合规性问题。现有方法在处理复杂的法律引用规则时，准确性不足，影响法律文书的有效性。

**核心思路**：通过构建一个包含866个蓝皮书任务的数据集，评估不同大型语言模型在遵循法律引用规则方面的能力，以验证其在法律实践中的适用性。

**技术框架**：研究采用了多种主流大型语言模型，包括OpenAI、Anthropic、Google、Meta和DeepSeek，进行系统性测试，比较它们在生成蓝皮书引用时的表现。

**关键创新**：本研究的创新点在于构建了专门针对蓝皮书引用的任务数据集，并系统评估了多种大型语言模型的合规性表现，填补了法律自动化领域的研究空白。

**关键设计**：在实验中，模型的输入包括蓝皮书的引用规则和示例，输出为生成的引用格式。通过对比分析，评估模型在不同任务下的表现，并探索上下文学习对准确率的影响。

## 📊 实验亮点

实验结果显示，测试的模型在生成合规蓝皮书引用时的准确率仅为69%-74%。即使通过上下文学习，准确率也仅提升至77%。这些数据表明，现成的LLMs在法律领域的应用仍需谨慎，特别是在程序遵循至关重要的情况下。

## 🎯 应用场景

该研究的潜在应用领域包括法律文书自动化生成、法律教育和法律技术工具的开发。通过提高大型语言模型在法律引用方面的准确性，可以减轻法律从业者的工作负担，提高法律文书的合规性和效率，推动法律行业的数字化转型。

## 📄 摘要（原文）

> Legal practice requires careful adherence to procedural rules. In the United States, few are more complex than those found in The Bluebook: A Uniform System of Citation. Compliance with this system's 500+ pages of byzantine formatting instructions is the raison d'etre of thousands of student law review editors and the bete noire of lawyers everywhere. To evaluate whether large language models (LLMs) are able to adhere to the procedures of such a complicated system, we construct an original dataset of 866 Bluebook tasks and test flagship LLMs from OpenAI, Anthropic, Google, Meta, and DeepSeek. We show (1) that these models produce fully compliant Bluebook citations only 69%-74% of the time and (2) that in-context learning on the Bluebook's underlying system of rules raises accuracy only to 77%. These results caution against using off-the-shelf LLMs to automate aspects of the law where fidelity to procedure is paramount.

