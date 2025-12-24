---
layout: default
title: "LaMPE: Length-aware Multi-grained Positional Encoding for Adaptive Long-context Scaling Without Training"
---

# LaMPE: Length-aware Multi-grained Positional Encoding for Adaptive Long-context Scaling Without Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02308" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02308v2</a>
  <a href="https://arxiv.org/pdf/2508.02308.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02308v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02308v2', 'LaMPE: Length-aware Multi-grained Positional Encoding for Adaptive Long-context Scaling Without Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sikui Zhang, Guangze Gao, Ziyun Gan, Chunfeng Yuan, Zefeng Lin, Houwen Peng, Bing Li, Weiming Hu

**分类**: cs.CL

**发布日期**: 2025-08-04 (更新: 2025-08-05)

**备注**: 13 pages, 9 figures

**🔗 代码/项目**: [GITHUB](https://github.com/scar-on/LaMPE)

---

## 💡 一句话要点

**提出LaMPE以解决长文本输入的性能下降问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本处理` `位置编码` `自适应模型` `多粒度注意力` `无训练方法`

## 📋 核心要点

1. 现有方法在处理超过预训练上下文窗口的输入时，性能显著下降，未能有效利用模型的上下文能力。
2. 本文提出的LaMPE通过动态映射输入长度与位置编码，优化了长文本的处理能力，避免了固定映射的局限性。
3. 在多个长上下文基准测试中，LaMPE相较于现有方法实现了显著的性能提升，展示了其有效性和适用性。

## 📝 摘要（中文）

大型语言模型（LLMs）在输入超过预训练上下文窗口时，性能显著下降，主要由于旋转位置嵌入（RoPE）的分布外（OOD）行为。现有研究通过固定映射策略缓解此问题，但忽略了输入长度与模型有效上下文窗口之间的动态关系。为此，本文提出了一种无训练的长度感知多粒度位置编码（LaMPE），充分利用模型的有效上下文窗口，实现LLMs的自适应长上下文扩展。LaMPE通过参数化的缩放sigmoid函数建立映射长度与输入长度之间的动态关系，并设计了一种新颖的多粒度注意力机制，战略性地在不同序列区域分配位置分辨率，以捕捉细粒度局部性和长距离依赖。实验表明，LaMPE在五个主流长上下文基准上显著提升了三种代表性LLMs的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在处理超出预训练上下文窗口的输入时，因旋转位置嵌入（RoPE）导致的性能下降问题。现有方法通过固定映射策略处理分布外（OOD）位置，但未能考虑输入长度与模型有效上下文窗口之间的动态关系。

**核心思路**：LaMPE的核心思路是通过参数化的缩放sigmoid函数，建立输入长度与位置编码之间的动态映射关系，从而自适应地分配位置编码的能力，优化长文本的处理。

**技术框架**：LaMPE的整体架构包括两个主要模块：一是长度感知的多粒度位置编码，二是多粒度注意力机制。前者负责动态调整位置编码，后者则在不同序列区域分配位置分辨率，以捕捉细粒度和长距离依赖。

**关键创新**：LaMPE的主要创新在于其训练无关性和动态映射能力，能够根据输入长度自适应调整位置编码，区别于传统的固定映射策略，显著提升了模型的上下文处理能力。

**关键设计**：在设计中，LaMPE采用了参数化的sigmoid函数来实现动态映射，并结合多粒度注意力机制，确保在不同序列区域内有效捕捉局部和全局信息。

## 📊 实验亮点

在对比实验中，LaMPE在五个主流长上下文基准上相较于现有长度外推方法实现了显著的性能提升，具体提升幅度达到XX%（具体数据待补充），展示了其在处理长文本输入时的有效性和优势。

## 🎯 应用场景

LaMPE的研究成果可广泛应用于自然语言处理领域，尤其是在需要处理长文本的任务中，如文档摘要、长篇对话生成等。其无训练的特性使得该方法能够快速集成到现有的RoPE基础模型中，提升模型的实际应用价值和灵活性。

## 📄 摘要（原文）

> Large language models (LLMs) experience significant performance degradation when the input exceeds the pretraining context window, primarily due to the out-of-distribution (OOD) behavior of Rotary Position Embedding (RoPE). Recent studies mitigate this problem by remapping OOD positions into the in-distribution range with fixed mapping strategies, ignoring the dynamic relationship between input length and the model's effective context window. To this end, we propose Length-aware Multi-grained Positional Encoding (LaMPE), a training-free method that fully utilizes the model's effective context window for adaptive long-context scaling in LLMs. Motivated by the left-skewed frequency distribution of relative positions, LaMPE establishes a dynamic relationship between mapping length and input length through a parametric scaled sigmoid function to adaptively allocate positional capacity across varying input lengths. Meanwhile, LaMPE devises a novel multi-grained attention mechanism that strategically allocates positional resolution across different sequence regions to capture both fine-grained locality and long-range dependencies. Our method can be seamlessly applied to a wide range of RoPE-based LLMs without training. Extensive experiments on three representative LLMs across five mainstream long-context benchmarks demonstrate that LaMPE achieves significant performance improvements compared to existing length extrapolation methods. The code will be released at https://github.com/scar-on/LaMPE.

