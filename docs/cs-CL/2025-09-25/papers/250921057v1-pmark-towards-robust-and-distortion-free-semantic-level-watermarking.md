---
layout: default
title: "PMark: Towards Robust and Distortion-free Semantic-level Watermarking with Channel Constraints"
---

# PMark: Towards Robust and Distortion-free Semantic-level Watermarking with Channel Constraints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21057" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21057v1</a>
  <a href="https://arxiv.org/pdf/2509.21057.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21057v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21057v1', 'PMark: Towards Robust and Distortion-free Semantic-level Watermarking with Channel Constraints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahao Huo, Shuliang Liu, Bin Wang, Junyan Zhang, Yibo Yan, Aiwei Liu, Xuming Hu, Mingxun Zhou

**分类**: cs.CR, cs.CL

**发布日期**: 2025-09-25

**🔗 代码/项目**: [GITHUB](https://github.com/PMark-repo/PMark)

---

## 💡 一句话要点

**PMark：基于通道约束的鲁棒无失真语义级水印方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语义级水印` `大型语言模型` `代理函数` `多通道约束` `鲁棒性` `无失真` `文本生成`

## 📋 核心要点

1. 现有语义级水印方法在面对释义攻击时鲁棒性不足，且基于拒绝采样的生成方式引入了显著的分布失真。
2. PMark通过引入代理函数概念，动态估计PF中位数并施加多通道约束，增强水印证据，从而提升鲁棒性。
3. 实验结果表明，PMark在文本质量和鲁棒性上均优于现有基线，为检测机器生成文本提供了更有效的方案。

## 📝 摘要（中文）

针对大型语言模型（LLM）的语义级水印（SWM）通过将句子作为基本单元，增强了水印对文本修改和释义攻击的鲁棒性。然而，现有方法仍然缺乏强大的鲁棒性理论保证，并且基于拒绝采样的生成方法通常会引入与未加水印输出相比显著的分布失真。本文通过代理函数（PF）的概念，引入了一个新的SWM理论框架，代理函数将句子映射到标量值。在此框架的基础上，我们提出了一种简单而强大的SWM方法PMark，该方法通过采样动态估计下一个句子的PF中位数，同时强制执行多个PF约束（我们称之为通道）以加强水印证据。PMark具有坚实的理论保证，实现了所需的无失真特性，并提高了对释义风格攻击的鲁棒性。我们还提供了一个经验优化的版本，进一步消除了动态中位数估计的需求，从而提高了采样效率。实验结果表明，PMark在文本质量和鲁棒性方面始终优于现有的SWM基线，为检测机器生成的文本提供了一种更有效的范例。我们的代码将在[this URL](https://github.com/PMark-repo/PMark)上发布。

## 🔬 方法详解

**问题定义**：论文旨在解决现有语义级水印方法在大型语言模型中应用时，鲁棒性不足和引入较大分布失真的问题。现有方法在面对释义攻击时容易失效，并且由于采用拒绝采样策略，生成文本的质量受到影响，与原始未加水印的文本存在较大差异。

**核心思路**：PMark的核心思路是利用代理函数（Proxy Function, PF）将句子映射到标量值，并通过控制这些标量值的分布来嵌入水印。通过动态估计PF中位数并施加多个PF约束（通道），可以更有效地嵌入和检测水印，同时减少对生成文本分布的干扰。这样设计的目的是在保证水印鲁棒性的同时，尽可能地保持生成文本的自然性和流畅性。

**技术框架**：PMark的整体框架包括以下几个主要步骤：1) 定义代理函数：选择合适的函数将句子映射到标量值。2) 动态中位数估计：通过采样估计下一个句子的PF中位数。3) 多通道约束：施加多个PF约束，形成多个水印通道，增强水印的强度和鲁棒性。4) 文本生成：根据估计的中位数和约束条件，生成带有水印的文本。5) 水印检测：通过分析生成文本的PF值，判断是否存在水印。

**关键创新**：PMark的关键创新在于引入了代理函数和多通道约束的概念，并在此基础上构建了一个新的语义级水印理论框架。与现有方法相比，PMark不仅提供了更强的鲁棒性理论保证，还通过动态中位数估计和多通道约束，显著减少了水印对生成文本分布的干扰，从而实现了无失真水印。

**关键设计**：PMark的关键设计包括：1) 代理函数的选择：选择合适的代理函数至关重要，需要考虑函数的计算效率和对文本语义的敏感性。2) 中位数估计方法：采用高效的采样方法来估计PF中位数，以减少计算开销。3) 通道数量和约束强度的设置：需要根据具体的应用场景和攻击模型，调整通道数量和约束强度，以达到最佳的鲁棒性和文本质量平衡。4) 经验优化版本：为了进一步提高采样效率，论文还提供了一个经验优化的版本，该版本消除了动态中位数估计的需求。

## 📊 实验亮点

实验结果表明，PMark在文本质量和鲁棒性方面均优于现有语义级水印基线方法。具体而言，PMark在保持文本质量的同时，显著提高了对释义攻击的抵抗能力，并且在水印检测准确率方面取得了显著提升。经验优化版本进一步提高了采样效率，使其更适用于实际应用场景。

## 🎯 应用场景

PMark可应用于检测大型语言模型生成的文本，防止恶意使用和版权侵犯。例如，可以用于识别AI生成的虚假新闻、学术论文抄袭检测、以及保护AI生成内容的知识产权。该技术有助于维护AI生态系统的健康发展，并促进AI技术的负责任使用。

## 📄 摘要（原文）

> Semantic-level watermarking (SWM) for large language models (LLMs) enhances watermarking robustness against text modifications and paraphrasing attacks by treating the sentence as the fundamental unit. However, existing methods still lack strong theoretical guarantees of robustness, and reject-sampling-based generation often introduces significant distribution distortions compared with unwatermarked outputs. In this work, we introduce a new theoretical framework on SWM through the concept of proxy functions (PFs) $\unicode{x2013}$ functions that map sentences to scalar values. Building on this framework, we propose PMark, a simple yet powerful SWM method that estimates the PF median for the next sentence dynamically through sampling while enforcing multiple PF constraints (which we call channels) to strengthen watermark evidence. Equipped with solid theoretical guarantees, PMark achieves the desired distortion-free property and improves the robustness against paraphrasing-style attacks. We also provide an empirically optimized version that further removes the requirement for dynamical median estimation for better sampling efficiency. Experimental results show that PMark consistently outperforms existing SWM baselines in both text quality and robustness, offering a more effective paradigm for detecting machine-generated text. Our code will be released at [this URL](https://github.com/PMark-repo/PMark).

