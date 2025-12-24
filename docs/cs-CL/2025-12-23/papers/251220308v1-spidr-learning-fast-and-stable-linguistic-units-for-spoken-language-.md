---
layout: default
title: SpidR: Learning Fast and Stable Linguistic Units for Spoken Language Models Without Supervision
---

# SpidR: Learning Fast and Stable Linguistic Units for Spoken Language Models Without Supervision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20308" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20308v1</a>
  <a href="https://arxiv.org/pdf/2512.20308.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20308v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20308v1', 'SpidR: Learning Fast and Stable Linguistic Units for Spoken Language Models Without Supervision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maxime Poli, Mahi Luthra, Youssef Benchekroun, Yosuke Higuchi, Martin Gleize, Jiayi Shen, Robin Algayres, Yu-An Chung, Mido Assran, Juan Pino, Emmanuel Dupoux

**分类**: cs.CL, cs.SD, eess.AS

**发布日期**: 2025-12-23

**备注**: 30 pages, 16 figures

**🔗 代码/项目**: [GITHUB](https://github.com/facebookresearch/spidr)

---

## 💡 一句话要点

**SpidR：无需监督，学习快速稳定的语音单元用于语音语言模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自监督学习` `语音表征学习` `语音语言模型` `自蒸馏` `在线聚类`

## 📋 核心要点

1. 现有语音语言模型依赖文本中间步骤，限制了其效率和泛化能力，SpidR旨在直接从语音中学习语言。
2. SpidR通过掩码预测、自蒸馏和在线聚类，学习具有高度可访问语音信息的语音表征，提升码本质量。
3. 实验表明，SpidR在多个语言建模基准上优于现有模型，并显著减少了预训练时间。

## 📝 摘要（中文）

语音语言建模和语音表征学习的并行发展，使得直接从语音中学习语言而无需文本中间步骤成为可能。本文提出了SpidR，一种自监督语音表征模型，它能高效地学习具有高度可访问语音信息的表征，特别适合于无文本语音语言建模。SpidR使用掩码预测目标、自蒸馏和在线聚类在原始波形上进行训练。学生模型的中间层学习预测来自教师模型中间层的分配。与以往方法相比，这种学习目标稳定了在线聚类过程，从而产生更高质量的码本。在下游语言建模基准测试（sWUGGY、sBLIMP、tSC）中，SpidR优于wav2vec 2.0、HuBERT、WavLM和DinoSR。此外，系统地评估了语音单元质量（ABX、PNMI）与语言建模性能之间的相关性，验证了这些指标作为可靠代理。最后，与HuBERT相比，SpidR显著减少了预训练时间，仅需在16个GPU上预训练一天，而不是一周。这种加速得益于预训练方法和高效的代码库，从而可以更快地迭代和更容易地进行实验。代码和模型检查点已开源。

## 🔬 方法详解

**问题定义**：本文旨在解决如何高效地从原始语音波形中学习高质量的语音表征，用于无文本语音语言建模。现有方法，如HuBERT，预训练时间长，且在线聚类过程不够稳定，导致学习到的语音单元质量不高。

**核心思路**：SpidR的核心思路是通过结合掩码预测、自蒸馏和在线聚类，稳定在线聚类过程，从而学习到具有高度可访问语音信息的语音表征。自蒸馏过程使得学生模型能够学习教师模型的知识，从而提高学习效率和稳定性。

**技术框架**：SpidR的整体框架包括一个学生模型和一个教师模型。首先，对原始语音波形进行掩码处理。然后，学生模型和教师模型分别对掩码后的语音进行编码。学生模型的中间层学习预测来自教师模型中间层的聚类分配。最后，通过掩码预测损失和自蒸馏损失来优化模型。

**关键创新**：SpidR的关键创新在于使用自蒸馏来稳定在线聚类过程。传统的在线聚类方法容易受到噪声和初始化影响，导致聚类结果不稳定。通过自蒸馏，学生模型可以学习教师模型的知识，从而提高聚类结果的稳定性和质量。

**关键设计**：SpidR的关键设计包括：1) 使用掩码预测目标来学习语音表征；2) 使用自蒸馏来稳定在线聚类过程；3) 使用在线聚类来生成语音单元的码本；4) 使用ABX和PNMI指标来评估语音单元的质量。具体的损失函数包括掩码预测损失和自蒸馏损失。网络结构基于Transformer架构。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20308v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20308v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20308v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SpidR在sWUGGY、sBLIMP和tSC等下游语言建模任务上优于wav2vec 2.0、HuBERT、WavLM和DinoSR等基线模型。更重要的是，SpidR显著减少了预训练时间，仅需在16个GPU上训练一天，而HuBERT需要一周。这使得SpidR更易于训练和部署。

## 🎯 应用场景

SpidR在语音识别、语音合成、语音翻译等领域具有广泛的应用前景。它可以用于构建端到端的语音处理系统，无需文本标注数据，降低了数据收集和标注的成本。此外，SpidR还可以用于跨语言语音处理，例如，在一种语言上训练的模型可以用于另一种语言的语音处理。

## 📄 摘要（原文）

> The parallel advances in language modeling and speech representation learning have raised the prospect of learning language directly from speech without textual intermediates. This requires extracting semantic representations directly from speech. Our contributions are threefold. First, we introduce SpidR, a self-supervised speech representation model that efficiently learns representations with highly accessible phonetic information, which makes it particularly suited for textless spoken language modeling. It is trained on raw waveforms using a masked prediction objective combined with self-distillation and online clustering. The intermediate layers of the student model learn to predict assignments derived from the teacher's intermediate layers. This learning objective stabilizes the online clustering procedure compared to previous approaches, resulting in higher quality codebooks. SpidR outperforms wav2vec 2.0, HuBERT, WavLM, and DinoSR on downstream language modeling benchmarks (sWUGGY, sBLIMP, tSC). Second, we systematically evaluate across models and layers the correlation between speech unit quality (ABX, PNMI) and language modeling performance, validating these metrics as reliable proxies. Finally, SpidR significantly reduces pretraining time compared to HuBERT, requiring only one day of pretraining on 16 GPUs, instead of a week. This speedup is enabled by the pretraining method and an efficient codebase, which allows faster iteration and easier experimentation. We open-source the training code and model checkpoints at https://github.com/facebookresearch/spidr.

