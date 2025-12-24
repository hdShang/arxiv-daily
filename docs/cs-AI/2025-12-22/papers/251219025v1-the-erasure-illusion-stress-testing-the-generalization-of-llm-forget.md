---
layout: default
title: "The Erasure Illusion: Stress-Testing the Generalization of LLM Forgetting Evaluation"
---

# The Erasure Illusion: Stress-Testing the Generalization of LLM Forgetting Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19025" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19025v1</a>
  <a href="https://arxiv.org/pdf/2512.19025.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19025v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19025v1', 'The Erasure Illusion: Stress-Testing the Generalization of LLM Forgetting Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hengrui Jia, Taoran Li, Jonas Guan, Varun Chandrasekaran

**分类**: cs.CR, cs.AI, cs.LG

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出Erasure Illusion框架，用于压力测试LLM遗忘评估的泛化能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器遗忘` `大型语言模型` `遗忘评估` `压力测试` `泛化能力` `AI安全` `数据隐私`

## 📋 核心要点

1. 现有LLM遗忘评估主要关注特定数据集上的性能下降，忽略了模型泛化能力带来的潜在知识残留。
2. 论文提出Erasure Illusion框架，通过生成语义相关的替代数据集，对遗忘评估指标进行压力测试。
3. 实验表明，现有遗忘指标经常高估LLM的遗忘效果，未能有效检测到模型保留的知识。

## 📝 摘要（中文）

机器遗忘旨在从已训练模型中移除特定数据的影响，这对于遵守版权法和确保AI安全至关重要。目前的遗忘指标通常通过监控模型在特定遗忘数据集 ($D_u$) 上的性能下降来衡量成功。我们认为，对于大型语言模型 (LLM) 来说，这种评估范式是不够的，并且可能具有误导性。许多现实世界中的遗忘应用（由版权或安全驱动）不仅针对 $D_u$ 中的逐字内容，还针对模型从中获得的更广泛的概括所影响的行为。我们证明，LLM 可以通过标准的遗忘评估，并且看起来已经“忘记”了目标知识，同时在语义上与 $D_u$ 相邻的内容上保持强大的能力。这种现象表明，擦除确切的句子并不一定等同于移除底层知识。为了解决这个差距，我们提出了 
ame，一个自动压力测试框架，用于生成替代数据集 $	ilde{D}_u$。构建该替代集，使其在语义上源自 $D_u$，但在嵌入空间中足够不同。通过比较 $D_u$ 和 $	ilde{D}_u$ 之间的遗忘指标分数，我们可以压力测试指标本身的可靠性。我们对三个 LLM 系列（Llama-3-8B、Qwen2.5-7B 和 Zephyr-7B-$β$）、三个不同的数据集和七个标准指标进行了广泛的评估，揭示了普遍的不一致性。我们发现，当前的指标经常高估遗忘的成功率，未能检测到我们的压力测试数据集暴露的保留知识。

## 🔬 方法详解

**问题定义**：现有LLM遗忘评估方法主要关注模型在特定遗忘数据集上的性能下降，而忽略了模型通过泛化学习到的知识的残留。这种评估方式无法有效衡量模型是否真正“忘记”了相关知识，存在被“欺骗”的风险。现有方法的痛点在于无法检测模型在语义相关的知识上的表现，从而可能导致对遗忘效果的过度乐观估计。

**核心思路**：论文的核心思路是通过构建与原始遗忘数据集语义相关但又足够不同的替代数据集，来对现有的遗忘评估指标进行压力测试。如果模型在原始数据集上表现出遗忘，但在替代数据集上仍然表现出相关知识，则说明现有的遗忘评估指标存在缺陷，无法准确衡量模型的遗忘效果。这种方法旨在揭示LLM遗忘评估中的“幻觉”，即模型表面上遗忘了某些信息，但实际上仍然保留了相关知识。

**技术框架**：Erasure Illusion框架主要包含以下几个阶段：1) 选择或构建原始遗忘数据集 ($D_u$)；2) 基于$D_u$，利用语义变换技术（例如释义、同义词替换等）生成替代数据集 ($	ilde{D}_u$)，确保$	ilde{D}_u$在语义上与$D_u$相关，但在嵌入空间中足够不同；3) 使用现有的遗忘评估指标分别在$D_u$和$	ilde{D}_u$上评估模型的遗忘效果；4) 比较在$D_u$和$	ilde{D}_u$上的评估结果，如果结果存在显著差异，则表明现有的遗忘评估指标存在问题。

**关键创新**：该论文最重要的技术创新点在于提出了一个通用的、自动化的压力测试框架，用于评估LLM遗忘评估指标的可靠性。与以往只关注特定数据集的遗忘评估方法不同，该框架通过引入语义相关的替代数据集，能够更全面地评估模型的遗忘效果，并揭示现有评估方法的局限性。这种方法为LLM遗忘评估提供了一个新的视角，有助于开发更可靠的遗忘评估指标。

**关键设计**：在替代数据集的生成过程中，需要仔细控制语义相似度和嵌入空间距离。论文可能使用了特定的语义变换技术和距离度量方法，以确保替代数据集既能反映原始数据集的语义信息，又能避免与原始数据集过于相似。此外，在比较评估结果时，可能需要使用统计检验方法来判断差异是否显著。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19025v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19025v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19025v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有的遗忘评估指标在面对Erasure Illusion框架生成的替代数据集时，经常表现出不一致性，高估了LLM的遗忘效果。在Llama-3-8B、Qwen2.5-7B和Zephyr-7B-$β$等多个LLM上，以及三个不同的数据集上，都观察到了这种现象。这表明现有的遗忘评估方法可能存在严重的缺陷，需要进一步改进。

## 🎯 应用场景

该研究成果可应用于评估和改进LLM的机器遗忘技术，确保模型能够有效移除特定数据的影响，从而更好地遵守版权法规、保护用户隐私，并提升AI系统的安全性。该框架能够帮助开发者识别和修复遗忘评估中的漏洞，开发更可靠的遗忘机制，从而构建更值得信赖的AI系统。

## 📄 摘要（原文）

> Machine unlearning aims to remove specific data influences from trained models, a capability essential for adhering to copyright laws and ensuring AI safety. Current unlearning metrics typically measure success by monitoring the model's performance degradation on the specific unlearning dataset ($D_u$). We argue that for Large Language Models (LLMs), this evaluation paradigm is insufficient and potentially misleading. Many real-world uses of unlearning--motivated by copyright or safety--implicitly target not only verbatim content in $D_u$, but also behaviors influenced by the broader generalizations the model derived from it. We demonstrate that LLMs can pass standard unlearning evaluation and appear to have ``forgotten'' the target knowledge, while simultaneously retaining strong capabilities on content that is semantically adjacent to $D_u$. This phenomenon indicates that erasing exact sentences does not necessarily equate to removing the underlying knowledge. To address this gap, we propose \name, an automated stress-testing framework that generates a surrogate dataset, $\tilde{D}_u$. This surrogate set is constructed to be semantically derived from $D_u$ yet sufficiently distinct in embedding space. By comparing unlearning metric scores between $D_u$ and $\tilde{D}_u$, we can stress-test the reliability of the metric itself. Our extensive evaluation across three LLM families (Llama-3-8B, Qwen2.5-7B, and Zephyr-7B-$β$), three distinct datasets, and seven standard metrics reveals widespread inconsistencies. We find that current metrics frequently overestimate unlearning success, failing to detect retained knowledge exposed by our stress-test datasets.

