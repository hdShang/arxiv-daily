---
layout: default
title: "Exploring Multimodal Challenges in Toxic Chinese Detection: Taxonomy, Benchmark, and Findings"
---

# Exploring Multimodal Challenges in Toxic Chinese Detection: Taxonomy, Benchmark, and Findings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24341" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24341v1</a>
  <a href="https://arxiv.org/pdf/2505.24341.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24341v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24341v1', 'Exploring Multimodal Challenges in Toxic Chinese Detection: Taxonomy, Benchmark, and Findings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shujian Yang, Shiyao Cui, Chuanrui Hu, Haicheng Wang, Tianwei Zhang, Minlie Huang, Jialiang Lu, Han Qiu

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2025-05-30

**备注**: Accepted to ACL 2025 (Findings). Camera-ready version

---

## 💡 一句话要点

**提出多模态挑战分类以提升中文毒性检测能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `毒性检测` `多模态挑战` `中文处理` `语言模型` `上下文学习` `监督微调` `数据集构建`

## 📋 核心要点

1. 现有的毒性检测方法在面对扰动的中文文本时表现不佳，容易被简单的字符替换所混淆。
2. 本文提出了一种三种扰动策略和八种具体方法的分类，旨在系统性地解决中文毒性检测中的多模态挑战。
3. 实验结果表明，当前的LLMs在检测扰动的毒性内容时能力不足，且在少量示例下可能出现误判现象。

## 📝 摘要（中文）

检测毒性内容在语言模型中至关重要，但面临诸多挑战。尽管大型语言模型（LLMs）在理解中文方面表现出色，研究表明简单的字符替换就能轻易混淆当前最先进的LLMs。本文强调中文语言的多模态特性是部署LLMs进行毒性检测的关键挑战。我们提出了三种扰动策略和八种具体方法的分类，并基于此分类整理了数据集，基准测试了九种来自美国和中国的最先进LLMs，以评估其对扰动毒性中文文本的检测能力。此外，我们探索了成本效益高的增强解决方案，如上下文学习（ICL）和监督微调（SFT）。结果显示，LLMs在检测扰动的多模态中文毒性内容方面能力较弱，且ICL或SFT在少量扰动示例下可能导致LLMs“过度校正”，将许多正常中文内容误判为毒性。

## 🔬 方法详解

**问题定义**：本文旨在解决中文毒性内容检测中，现有方法对扰动文本的识别能力不足的问题。简单的字符替换会导致LLMs的检测效果显著下降。

**核心思路**：我们提出了一种新的分类方法，针对中文毒性内容的多模态特性，设计了三种扰动策略和八种具体方法，以增强LLMs的检测能力。

**技术框架**：整体架构包括数据集的构建、扰动策略的应用以及对九种LLMs的基准测试。主要模块包括数据预处理、模型训练和性能评估。

**关键创新**：最重要的创新在于提出了针对中文毒性检测的多模态扰动分类，这一方法与现有的单一文本检测方法有本质区别，能够更全面地评估模型的鲁棒性。

**关键设计**：在模型训练中，我们采用了上下文学习（ICL）和监督微调（SFT）等技术，设置了特定的损失函数以优化模型在扰动文本上的表现。

## 📊 实验亮点

实验结果显示，当前的LLMs在检测扰动的多模态中文毒性内容时表现不佳，准确率显著低于对未扰动文本的检测。此外，使用ICL或SFT时，模型在少量扰动示例下的误判率增加，导致正常内容被错误标记为毒性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体监控、在线评论审核和内容过滤等，能够有效提升对中文毒性内容的检测能力，具有重要的社会价值和实际意义。未来，该方法可扩展至其他语言的毒性检测任务，推动多模态内容分析的发展。

## 📄 摘要（原文）

> Detecting toxic content using language models is important but challenging. While large language models (LLMs) have demonstrated strong performance in understanding Chinese, recent studies show that simple character substitutions in toxic Chinese text can easily confuse the state-of-the-art (SOTA) LLMs. In this paper, we highlight the multimodal nature of Chinese language as a key challenge for deploying LLMs in toxic Chinese detection. First, we propose a taxonomy of 3 perturbation strategies and 8 specific approaches in toxic Chinese content. Then, we curate a dataset based on this taxonomy, and benchmark 9 SOTA LLMs (from both the US and China) to assess if they can detect perturbed toxic Chinese text. Additionally, we explore cost-effective enhancement solutions like in-context learning (ICL) and supervised fine-tuning (SFT). Our results reveal two important findings. (1) LLMs are less capable of detecting perturbed multimodal Chinese toxic contents. (2) ICL or SFT with a small number of perturbed examples may cause the LLMs "overcorrect'': misidentify many normal Chinese contents as toxic.

