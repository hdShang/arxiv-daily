---
layout: default
title: "TraceDet: Hallucination Detection from the Decoding Trace of Diffusion Large Language Models"
---

# TraceDet: Hallucination Detection from the Decoding Trace of Diffusion Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01274" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01274v1</a>
  <a href="https://arxiv.org/pdf/2510.01274.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01274v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01274v1', 'TraceDet: Hallucination Detection from the Decoding Trace of Diffusion Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shenxu Chang, Junchi Yu, Weixing Wang, Yongqiang Chen, Jialin Yu, Philip Torr, Jindong Gu

**分类**: cs.CL, cs.LG

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**TraceDet：利用扩散大语言模型解码轨迹进行幻觉检测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `大语言模型` `幻觉检测` `去噪过程` `动作轨迹`

## 📋 核心要点

1. 现有的幻觉检测方法主要针对自回归模型，无法有效利用扩散模型多步去噪过程中的幻觉信号。
2. TraceDet将扩散模型的去噪过程建模为动作轨迹，通过分析中间步骤预测来识别幻觉。
3. 实验表明，TraceDet在幻觉检测方面显著优于现有方法，AUROC平均提升15.2%。

## 📝 摘要（中文）

扩散大语言模型（D-LLMs）作为自回归LLM（AR-LLMs）的一种有前景的替代方案而崭露头角。然而，D-LLM中的幻觉问题仍未得到充分研究，限制了它们在实际应用中的可靠性。现有的幻觉检测方法是为AR-LLM设计的，依赖于单步生成中的信号，因此不适用于D-LLM，因为幻觉信号通常在多步去噪过程中出现。为了弥合这一差距，我们提出了TraceDet，这是一个新颖的框架，它显式地利用D-LLM的中间去噪步骤进行幻觉检测。TraceDet将去噪过程建模为一个动作轨迹，每个动作被定义为模型对清理后的响应的预测，并以先前的中间输出为条件。通过识别对幻觉响应信息量最大的子轨迹，TraceDet利用D-LLM多步去噪过程中的关键幻觉信号进行幻觉检测。在各种开源D-LLM上进行的大量实验表明，与基线相比，TraceDet始终提高了幻觉检测能力，AUROC平均提高了15.2%。

## 🔬 方法详解

**问题定义**：论文旨在解决扩散大语言模型（D-LLMs）中存在的幻觉问题。现有的幻觉检测方法主要针对自回归模型（AR-LLMs），依赖于单步生成过程中的信号，无法有效捕捉D-LLMs在多步去噪过程中产生的幻觉信号。因此，如何充分利用D-LLMs的中间去噪步骤进行幻觉检测是一个关键挑战。

**核心思路**：论文的核心思路是将D-LLMs的去噪过程建模为一个动作轨迹（action trace），其中每个动作代表模型在给定先前中间输出的情况下，对清理后的响应的预测。通过分析这个轨迹，可以识别出对幻觉响应信息量最大的子轨迹，从而提取关键的幻觉信号。这种方法能够更全面地捕捉D-LLMs在多步去噪过程中产生的幻觉。

**技术框架**：TraceDet框架主要包含以下几个阶段：1) 将D-LLM的去噪过程展开为一系列中间步骤；2) 将每个中间步骤的预测视为一个动作，构建动作轨迹；3) 利用模型学习每个动作对最终输出的影响，并识别出对幻觉响应影响最大的子轨迹；4) 基于识别出的子轨迹进行幻觉检测。

**关键创新**：该论文的关键创新在于显式地利用了D-LLMs的中间去噪步骤进行幻觉检测。与现有方法仅关注最终输出或单步生成过程不同，TraceDet通过建模去噪轨迹，能够更全面地捕捉D-LLMs在多步去噪过程中产生的幻觉信号。这种方法更适合D-LLMs的特性，并能有效提高幻觉检测的准确性。

**关键设计**：TraceDet的关键设计包括：1) 如何定义和表示动作轨迹，即如何将D-LLM的中间步骤转化为可分析的动作序列；2) 如何学习每个动作对最终输出的影响，例如可以使用注意力机制或强化学习等方法；3) 如何识别对幻觉响应信息量最大的子轨迹，例如可以使用信息增益或互信息等指标；4) 如何基于识别出的子轨迹进行幻觉检测，例如可以使用分类器或回归模型。

## 📊 实验亮点

实验结果表明，TraceDet在各种开源D-LLM上均能显著提高幻觉检测的性能，AUROC平均提升15.2%。这一结果表明，TraceDet能够有效利用D-LLM的中间去噪步骤进行幻觉检测，并优于现有的基线方法。该研究为D-LLM的幻觉检测提供了一种新的有效途径。

## 🎯 应用场景

TraceDet可应用于各种基于扩散模型的自然语言生成任务，例如文本摘要、机器翻译、对话生成等。通过提高扩散模型的可靠性，TraceDet有助于在实际应用中减少错误信息的产生，提升用户体验，并降低潜在风险。该研究对于推动扩散模型在安全关键领域的应用具有重要意义。

## 📄 摘要（原文）

> Diffusion large language models (D-LLMs) have recently emerged as a promising alternative to auto-regressive LLMs (AR-LLMs). However, the hallucination problem in D-LLMs remains underexplored, limiting their reliability in real-world applications. Existing hallucination detection methods are designed for AR-LLMs and rely on signals from single-step generation, making them ill-suited for D-LLMs where hallucination signals often emerge throughout the multi-step denoising process. To bridge this gap, we propose TraceDet, a novel framework that explicitly leverages the intermediate denoising steps of D-LLMs for hallucination detection. TraceDet models the denoising process as an action trace, with each action defined as the model's prediction over the cleaned response, conditioned on the previous intermediate output. By identifying the sub-trace that is maximally informative to the hallucinated responses, TraceDet leverages the key hallucination signals in the multi-step denoising process of D-LLMs for hallucination detection. Extensive experiments on various open source D-LLMs demonstrate that TraceDet consistently improves hallucination detection, achieving an average gain in AUROC of 15.2% compared to baselines.

