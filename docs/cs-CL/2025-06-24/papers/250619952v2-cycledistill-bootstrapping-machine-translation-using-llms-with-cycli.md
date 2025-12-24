---
layout: default
title: "CycleDistill: Bootstrapping Machine Translation using LLMs with Cyclical Distillation"
---

# CycleDistill: Bootstrapping Machine Translation using LLMs with Cyclical Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19952" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19952v2</a>
  <a href="https://arxiv.org/pdf/2506.19952.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19952v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19952v2', 'CycleDistill: Bootstrapping Machine Translation using LLMs with Cyclical Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Deepon Halder, Thanmay Jayakumar, Raj Dabre

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-24 (更新: 2025-08-09)

---

## 💡 一句话要点

**提出CycleDistill以解决低资源语言机器翻译问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器翻译` `低资源语言` `大型语言模型` `合成平行语料` `蒸馏训练` `少样本学习` `翻译质量提升`

## 📋 核心要点

1. 现有的机器翻译系统在低资源语言上缺乏足够的平行语料，导致翻译质量不高。
2. CycleDistill通过迭代生成合成平行语料库，利用LLMs和少量样本翻译来提升机器翻译质量。
3. 在实验中，CycleDistill在三种印度语言上实现了20-30 chrF点的显著提升，展示了其有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）在少量样本机器翻译（MT）方面表现出色，但在高质量机器翻译上仍不及专门训练的MT系统，尤其是在低资源语言中。本文提出CycleDistill，一种利用LLMs和少量样本翻译的引导方法，通过零样本或少样本MT从单语语料库迭代生成合成平行语料库，进而微调模型。CycleDistill仅需1至4个少量样本示例，依靠单语语料库即可实现高质量机器翻译。在针对三种印度语言的实验中，CycleDistill在首次迭代中平均提高了20-30个chrF点。此外，研究还探讨了在蒸馏过程中利用softmax激活的效果，观察到翻译质量的轻微提升。

## 🔬 方法详解

**问题定义**：本文旨在解决低资源语言机器翻译中平行语料稀缺的问题。现有方法依赖大量平行语料，导致在低资源语言上表现不佳。

**核心思路**：CycleDistill的核心思路是通过迭代生成合成平行语料库，利用LLMs进行零样本或少样本翻译，从而减少对平行语料的依赖。

**技术框架**：该方法的整体架构包括几个主要阶段：首先，从单语语料库生成合成平行语料；然后，使用生成的平行语料微调翻译模型；最后，重复这一过程以进一步提升翻译质量。

**关键创新**：CycleDistill的创新在于其迭代生成合成平行语料的能力，使得在缺乏平行语料的情况下仍能实现高质量翻译。这一方法与传统依赖大量平行语料的方式本质上不同。

**关键设计**：在模型微调过程中，CycleDistill仅需1至4个少量样本示例，并且在蒸馏过程中引入softmax激活以提升翻译质量。

## 📊 实验亮点

在针对三种印度语言的实验中，CycleDistill在首次迭代中平均提高了20-30个chrF点，相较于少样本基线模型表现出显著的翻译质量提升，验证了其有效性和创新性。

## 🎯 应用场景

CycleDistill的研究成果在低资源语言的机器翻译领域具有广泛的应用潜力，能够帮助提升这些语言的翻译质量，促进跨语言交流和信息获取。此外，该方法的灵活性使其适用于多种语言对的翻译任务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs), despite their ability to perform few-shot machine translation (MT), often lag behind dedicated MT systems trained on parallel corpora, which are crucial for high quality machine translation (MT). However, parallel corpora are often scarce or non-existent for low-resource languages. In this paper, we propose CycleDistill, a bootstrapping approach leveraging LLMs and few-shot translation to obtain high-quality MT systems. CycleDistill involves iteratively generating synthetic parallel corpora from monolingual corpora via zero- or few-shot MT, which is then used to fine-tune the model that was used for generating said data for MT. CycleDistill does not need parallel corpora beyond 1 to 4 few-shot examples, and in our experiments focusing on three Indian languages, by relying solely on monolingual corpora, it can achieve high-quality machine translation, improving upon a few-shot baseline model by over 20-30 chrF points on average in the first iteration. We also study the effect of leveraging softmax activations during the distillation process and observe mild improvements in translation quality.

