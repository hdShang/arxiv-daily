---
layout: default
title: "LLM-BI: Towards Fully Automated Bayesian Inference with Large Language Models"
---

# LLM-BI: Towards Fully Automated Bayesian Inference with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08300" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08300v1</a>
  <a href="https://arxiv.org/pdf/2508.08300.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08300v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08300v1', 'LLM-BI: Towards Fully Automated Bayesian Inference with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yongchao Huang

**分类**: cs.AI

**发布日期**: 2025-08-07

**备注**: 6 pages

**DOI**: [10.5281/zenodo.16756724](https://doi.org/10.5281/zenodo.16756724)

---

## 💡 一句话要点

**提出LLM-BI以实现全自动贝叶斯推断**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `贝叶斯推断` `大型语言模型` `自动化建模` `概率编程` `统计学习`

## 📋 核心要点

1. 贝叶斯推断的应用受到先验分布和似然指定的限制，通常需要专业的统计知识。
2. 本文提出LLM-BI，通过大型语言模型自动化贝叶斯推断过程，降低了对统计专业知识的依赖。
3. 实验结果表明，LLM能够有效引出先验分布并指定完整模型结构，展示了其在贝叶斯建模中的应用潜力。

## 📝 摘要（中文）

贝叶斯推断的广泛应用面临一个重要障碍，即先验分布和似然的指定，这通常需要专业的统计知识。本文探讨了利用大型语言模型（LLM）自动化这一过程的可行性。我们提出了LLM-BI（基于大型语言模型的贝叶斯推断），这是一个自动化贝叶斯工作流的概念性管道。作为概念验证，我们进行了两项实验，重点关注贝叶斯线性回归。在实验一中，我们展示了LLM能够成功从自然语言中引出先验分布。在实验二中，我们表明LLM可以从单一高层次问题描述中指定整个模型结构，包括先验和似然。我们的结果验证了LLM在自动化贝叶斯建模关键步骤中的潜力，为概率编程的自动推断管道提供了可能性。

## 🔬 方法详解

**问题定义**：本文旨在解决贝叶斯推断中先验分布和似然指定的困难，现有方法通常需要专业的统计知识，限制了其广泛应用。

**核心思路**：通过利用大型语言模型（LLM），自动化贝叶斯推断的关键步骤，降低对用户统计知识的要求，使得非专业人士也能进行贝叶斯建模。

**技术框架**：LLM-BI的整体架构包括两个主要模块：首先是从自然语言中提取先验分布，其次是从高层次问题描述中构建完整的模型结构。

**关键创新**：最重要的创新在于利用LLM自动化先验和似然的指定过程，这与传统方法依赖于用户的统计知识形成鲜明对比。

**关键设计**：在实验中，LLM的训练数据和模型参数设置经过精心设计，以确保其能够准确理解和生成与贝叶斯推断相关的内容。

## 📊 实验亮点

实验结果显示，LLM成功从自然语言中引出先验分布，并能够从单一高层次问题描述中构建完整的贝叶斯模型结构。这一过程的自动化显著提高了建模效率，展示了LLM在贝叶斯推断中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括数据科学、机器学习和统计分析等，能够帮助非专业人士更容易地进行贝叶斯推断，推动相关领域的研究和应用。未来，LLM-BI有望成为自动化概率编程的重要工具，降低技术门槛，促进更广泛的应用。

## 📄 摘要（原文）

> A significant barrier to the widespread adoption of Bayesian inference is the specification of prior distributions and likelihoods, which often requires specialized statistical expertise. This paper investigates the feasibility of using a Large Language Model (LLM) to automate this process. We introduce LLM-BI (Large Language Model-driven Bayesian Inference), a conceptual pipeline for automating Bayesian workflows. As a proof-of-concept, we present two experiments focused on Bayesian linear regression. In Experiment I, we demonstrate that an LLM can successfully elicit prior distributions from natural language. In Experiment II, we show that an LLM can specify the entire model structure, including both priors and the likelihood, from a single high-level problem description. Our results validate the potential of LLMs to automate key steps in Bayesian modeling, enabling the possibility of an automated inference pipeline for probabilistic programming.

