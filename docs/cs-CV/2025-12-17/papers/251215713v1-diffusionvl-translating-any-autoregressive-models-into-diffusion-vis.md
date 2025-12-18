---
layout: default
title: DiffusionVL: Translating Any Autoregressive Models into Diffusion Vision Language Models
---

# DiffusionVL: Translating Any Autoregressive Models into Diffusion Vision Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15713" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15713v1</a>
  <a href="https://arxiv.org/pdf/2512.15713.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15713v1" onclick="toggleFavorite(this, '2512.15713v1', 'DiffusionVL: Translating Any Autoregressive Models into Diffusion Vision Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lunbin Zeng, Jingfeng Yao, Bencheng Liao, Hongyuan Tao, Wenyu Liu, Xinggang Wang

**分类**: cs.CV

**发布日期**: 2025-12-17

**备注**: 11 pages, 5 figures, conference or other essential info

**🔗 代码/项目**: [GITHUB](https://github.com/hustvl/DiffusionVL)

---

## 💡 一句话要点

**DiffusionVL：将任意自回归模型转化为扩散视觉语言模型，提升性能与推理速度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `视觉语言模型` `自回归模型` `多模态学习` `范式转换` `预训练模型` `微调` `块解码`

## 📋 核心要点

1. 现有的扩散视觉语言模型（dVLM）由于基础扩散语言模型的能力限制，性能显著落后于主流的自回归（AR）模型。
2. DiffusionVL的核心思想是将现有的强大AR模型转化为dVLM，通过简单的微调即可实现范式转换，充分利用了AR模型的预训练知识。
3. 实验表明，DiffusionVL在数据量远小于先前方法的情况下，性能取得了显著提升，并在推理速度上实现了2倍的加速。

## 📝 摘要（中文）

本文提出了DiffusionVL，一个可以从任何强大的自回归（AR）模型转换而来的扩散视觉语言模型（dVLM）家族。通过简单的微调，成功地将AR预训练模型适配到扩散范式。研究发现：从基于AR的多模态模型到扩散的范式转变非常有效；直接将AR语言模型转换为dVLM也是可行的，其性能与LLaVA风格的视觉指令调优模型具有竞争力。此外，本文在dVLM中引入了块解码设计，支持任意长度生成和KV缓存重用，从而显著提高了推理速度。大量实验表明，DiffusionVL仅使用不到先前方法5%的数据进行训练，就在MMMU-Pro（视觉）基准测试中获得了34.4%的增益，在MME（认知）基准测试中获得了37.5%的增益，同时推理速度提高了2倍。

## 🔬 方法详解

**问题定义**：现有扩散视觉语言模型(dVLM)的性能受限于其基础扩散语言模型的能力，与主流的自回归(AR)模型相比存在显著差距。因此，如何利用已有的强大AR模型来构建高性能的dVLM是一个关键问题。现有方法通常需要从头开始训练扩散模型，计算成本高昂，且难以达到AR模型的性能水平。

**核心思路**：DiffusionVL的核心思路是将预训练的AR模型转化为扩散模型，从而继承AR模型的强大语言能力。通过微调，使AR模型能够生成扩散模型所需的噪声预测，避免了从头训练扩散模型的高成本。这种范式转换能够充分利用AR模型的预训练知识，从而快速构建高性能的dVLM。

**技术框架**：DiffusionVL的整体框架包括以下几个主要步骤：1) 选择一个预训练的AR模型作为基础模型。2) 在AR模型的基础上添加一个噪声预测头，用于预测扩散过程中的噪声。3) 使用视觉-语言数据集对模型进行微调，使模型能够根据图像和文本输入预测噪声。4) 在推理阶段，使用扩散模型进行文本生成，通过迭代去噪过程生成最终的文本输出。该框架支持块解码设计，允许任意长度的文本生成，并支持KV缓存重用以加速推理。

**关键创新**：DiffusionVL的关键创新在于将AR模型转化为扩散模型，实现了范式上的转变。与传统的从头训练扩散模型的方法相比，DiffusionVL能够更有效地利用预训练知识，从而在更少的数据上达到更高的性能。此外，块解码设计和KV缓存重用进一步提高了推理效率。

**关键设计**：DiffusionVL的关键设计包括：1) 噪声预测头的结构，需要与AR模型的输出相匹配。2) 微调策略，需要平衡AR模型的语言能力和扩散模型的生成能力。3) 块解码的实现细节，需要保证生成文本的连贯性和一致性。4) 损失函数的设计，需要同时考虑噪声预测的准确性和生成文本的质量。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15713v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15713v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15713v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DiffusionVL在多个视觉-语言基准测试中取得了显著的性能提升。在MMMU-Pro（视觉）基准测试中，DiffusionVL获得了34.4%的增益；在MME（认知）基准测试中，获得了37.5%的增益。更重要的是，DiffusionVL仅使用不到先前方法5%的数据进行训练，并且推理速度提高了2倍。这些结果表明，DiffusionVL是一种高效且有效的视觉-语言模型。

## 🎯 应用场景

DiffusionVL具有广泛的应用前景，包括图像描述、视觉问答、图像生成、视觉对话等。该模型可以应用于智能客服、教育辅助、内容创作等领域，为用户提供更智能、更高效的视觉-语言交互体验。未来，DiffusionVL有望成为多模态人工智能领域的重要基石。

## 📄 摘要（原文）

> In recent multimodal research, the diffusion paradigm has emerged as a promising alternative to the autoregressive paradigm (AR), owing to its unique decoding advantages. However, due to the capability limitations of the base diffusion language model, the performance of the diffusion vision language model (dVLM) still lags significantly behind that of mainstream models. This leads to a simple yet fundamental question: Is it possible to construct dVLMs based on existing powerful AR models? In response, we propose DiffusionVL, a dVLM family that could be translated from any powerful AR models. Through simple fine-tuning, we successfully adapt AR pre-trained models into the diffusion paradigm. This approach yields two key observations: (1) The paradigm shift from AR-based multimodal models to diffusion is remarkably effective. (2) Direct conversion of an AR language model to a dVLM is also feasible, achieving performance competitive with LLaVA-style visual-instruction-tuning. Further, we introduce a block-decoding design into dVLMs that supports arbitrary-length generation and KV cache reuse, achieving a significant inference speedup. We conduct a large number of experiments. Despite training with less than 5% of the data required by prior methods, DiffusionVL achieves a comprehensive performance improvement-a 34.4% gain on the MMMU-Pro (vision) bench and 37.5% gain on the MME (Cog.) bench-alongside a 2x inference speedup. The model and code are released at https://github.com/hustvl/DiffusionVL.

