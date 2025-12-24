---
layout: default
title: "FAID: Fine-Grained AI-Generated Text Detection Using Multi-Task Auxiliary and Multi-Level Contrastive Learning"
---

# FAID: Fine-Grained AI-Generated Text Detection Using Multi-Task Auxiliary and Multi-Level Contrastive Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14271" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14271v2</a>
  <a href="https://arxiv.org/pdf/2505.14271.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14271v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14271v2', 'FAID: Fine-Grained AI-Generated Text Detection Using Multi-Task Auxiliary and Multi-Level Contrastive Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minh Ngoc Ta, Dong Cao Van, Duc-Anh Hoang, Minh Le-Anh, Truong Nguyen, My Anh Tran Nguyen, Yuxia Wang, Preslav Nakov, Sang Dinh

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-10-07)

---

## 💡 一句话要点

**提出FAID框架以解决AI生成文本的细粒度检测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `文本检测` `AI生成` `多任务学习` `对比学习` `细粒度分类` `LLM识别` `风格特征`

## 📋 核心要点

1. 现有方法在区分人类撰写和AI生成文本时存在局限，无法有效处理人类与LLM协作生成的文本。
2. 本文提出的FAID框架结合多级对比学习和多任务辅助分类，旨在捕捉文本的细微风格特征，并识别生成器的LLM家族。
3. 实验结果显示，FAID在多个基线模型上表现优越，尤其在未见领域和新LLM上的泛化能力显著增强。

## 📝 摘要（中文）

随着人类与AI模型在生成任务中的合作日益增多，区分人类撰写、LLM生成和人类-LLM协作文本的挑战也随之而来。本文收集了一个多语言、多领域、多生成器的数据集FAIDSet，并提出了细粒度检测框架FAID，能够将文本分类为这三种类别，并识别生成器的LLM家族。FAID通过结合多级对比学习和多任务辅助分类，捕捉细微的风格线索，适应分布变化而无需重新训练。实验结果表明，FAID在未见领域和新LLM上的泛化准确性显著提升，为提高AI辅助写作的透明度和问责制提供了潜在解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决人类撰写、LLM生成和人类-LLM协作文本的细粒度检测问题。现有方法多为二分类器，无法有效捕捉文本的作者特征和模型特性。

**核心思路**：FAID框架通过多级对比学习与多任务辅助分类相结合，能够学习到文本中的细微风格线索，并将不同的LLM家族视为独特的风格实体，从而提高检测的准确性。

**技术框架**：FAID的整体架构包括数据预处理、特征提取、对比学习模块和分类模块。通过多任务学习，模型能够同时进行文本分类和LLM家族识别。

**关键创新**：FAID的主要创新在于其细粒度的检测能力，能够同时捕捉文本的作者特征和模型特性，克服了传统方法的局限。

**关键设计**：在模型设计中，采用了多级对比损失函数，以增强模型对细微风格差异的敏感性，同时设置了适应性机制，以应对分布变化而无需重新训练。

## 📊 实验亮点

实验结果表明，FAID在多个基线模型上表现优越，尤其在未见领域和新LLM上的泛化准确性提升了显著，具体提升幅度达到XX%（具体数据待补充），展示了其在实际应用中的有效性和可靠性。

## 🎯 应用场景

FAID框架在文本生成和检测领域具有广泛的应用潜力，尤其是在内容审核、学术诚信检测和AI写作工具的透明性提升方面。随着AI生成文本的普及，FAID能够帮助用户更好地理解文本来源，增强对AI生成内容的信任。未来，该技术可能在教育、媒体和法律等多个领域产生深远影响。

## 📄 摘要（原文）

> The growing collaboration between humans and AI models in generative tasks has introduced new challenges in distinguishing between human-written, LLM-generated, and human--LLM collaborative texts. In this work, we collect a multilingual, multi-domain, multi-generator dataset FAIDSet. We further introduce a fine-grained detection framework FAID to classify text into these three categories, and also to identify the underlying LLM family of the generator. Unlike existing binary classifiers, FAID is built to capture both authorship and model-specific characteristics. Our method combines multi-level contrastive learning with multi-task auxiliary classification to learn subtle stylistic cues. By modeling LLM families as distinct stylistic entities, we incorporate an adaptation to address distributional shifts without retraining for unseen data. Our experimental results demonstrate that FAID outperforms several baselines, particularly enhancing the generalization accuracy on unseen domains and new LLMs, thus offering a potential solution for improving transparency and accountability in AI-assisted writing.

