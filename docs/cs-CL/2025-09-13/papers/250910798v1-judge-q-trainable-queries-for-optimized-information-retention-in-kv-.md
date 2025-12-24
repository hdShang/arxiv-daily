---
layout: default
title: "Judge Q: Trainable Queries for Optimized Information Retention in KV Cache Eviction"
---

# Judge Q: Trainable Queries for Optimized Information Retention in KV Cache Eviction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10798" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10798v1</a>
  <a href="https://arxiv.org/pdf/2509.10798.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10798v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10798v1', 'Judge Q: Trainable Queries for Optimized Information Retention in KV Cache Eviction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yijun Liu, Yixuan Wang, Yuzhuang Xu, Shiyu Ji, Yang Xu, Qingfu Zhu, Wanxiang Che

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-13

**备注**: preprint

---

## 💡 一句话要点

**Judge Q：通过可训练查询优化KV缓存淘汰中的信息保留**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `KV缓存淘汰` `长序列建模` `注意力机制` `全局信息` `软Token`

## 📋 核心要点

1. 现有KV缓存淘汰方法过度关注局部信息，忽略全局信息，导致性能下降。
2. Judge Q通过引入可训练的软token列表，使查询能够捕获全局信息，从而更准确地评估KV缓存的重要性。
3. 实验表明，Judge Q在LongBench和RULER等基准测试中，性能优于现有方法，且训练开销极小。

## 📝 摘要（中文）

大型语言模型（LLMs）利用键值（KV）缓存来存储序列处理过程中的历史信息。KV缓存的大小随着序列长度的增加而线性增长，严重影响内存使用和解码效率。现有的KV缓存淘汰方法通常使用预填充阶段的最后一个窗口作为查询，以计算KV重要性得分进行淘汰。虽然这种方案易于实现，但它往往过度关注局部信息，可能导致忽略或遗漏关键的全局信息。为了缓解这个问题，我们提出了一种新的训练方法Judge Q，该方法结合了一个软token列表。该方法仅以较低的训练成本调整模型的嵌入层。通过将软token列表连接到输入序列的末尾，我们训练这些token的注意力图与原始输入序列的注意力图对齐，使其与实际解码token的注意力图对齐。这样，与软token对应的查询可以有效地捕获全局信息，并更好地评估KV缓存中键和值的重要性，从而在KV缓存被淘汰时保持解码质量。在相同的淘汰预算下，我们的方法比现有的淘汰方法表现出更少的性能下降。我们通过在Llama-3.1-8B-Instruct和Mistral-7B-Instruct-v0.3等模型上进行的实验验证了我们的方法，使用了包括LongBench、RULER和Needle-in-a-Haystack在内的基准。结果表明，LongBench上的改进约为1个点，RULER上的改进超过3个点。这种提出的方法可以无缝地集成到现有的开源模型中，只需极少的训练开销，从而提高KV缓存淘汰场景中的性能。

## 🔬 方法详解

**问题定义**：大型语言模型在处理长序列时，KV缓存会线性增长，导致内存占用过高和解码效率降低。现有的KV缓存淘汰策略，例如使用预填充阶段的最后窗口作为查询，往往只关注局部信息，无法有效识别和保留全局重要信息，从而影响模型性能。

**核心思路**：Judge Q的核心思路是通过训练一组软token，使其能够捕获输入序列的全局信息。这些软token被添加到输入序列的末尾，并通过训练，使其对原始输入序列的注意力分布与实际解码token的注意力分布对齐。这样，软token对应的查询就能更全面地评估KV缓存中键和值的重要性。

**技术框架**：Judge Q的整体框架包括以下步骤：1) 在原始输入序列后添加一组可训练的软token。2) 使用语言模型处理包含软token的序列。3) 计算软token对原始输入序列的注意力图。4) 使用损失函数，使软token的注意力图与实际解码token的注意力图对齐。5) 使用训练好的软token作为查询，评估KV缓存中键和值的重要性，并进行淘汰。

**关键创新**：Judge Q的关键创新在于引入了可训练的软token列表，并使用注意力对齐的方式，使这些软token能够捕获全局信息。与现有方法相比，Judge Q不再局限于局部信息，而是能够更全面地评估KV缓存的重要性。此外，Judge Q只需要调整模型的嵌入层，训练成本非常低。

**关键设计**：Judge Q的关键设计包括：1) 软token的数量：需要根据具体任务和模型进行调整。2) 注意力对齐的损失函数：可以使用KL散度或交叉熵等损失函数，衡量软token的注意力图与实际解码token的注意力图之间的差异。3) 训练策略：可以使用Adam等优化器，并设置合适的学习率和训练轮数。

## 📊 实验亮点

实验结果表明，Judge Q在LongBench上提升了约1个点，在RULER上提升了超过3个点。这些提升是在相同的淘汰预算下实现的，表明Judge Q能够更有效地利用有限的KV缓存资源。此外，Judge Q的训练开销极小，可以轻松集成到现有的开源模型中。

## 🎯 应用场景

Judge Q可应用于各种需要处理长序列的大型语言模型，例如文档摘要、机器翻译、对话生成等。通过优化KV缓存淘汰策略，Judge Q可以显著降低内存占用，提高解码效率，从而使这些模型能够在资源受限的环境中运行，并处理更长的序列。该方法具有广泛的应用前景和实际价值。

## 📄 摘要（原文）

> Large language models (LLMs) utilize key-value (KV) cache to store historical information during sequence processing. The size of KV cache grows linearly as the length of the sequence extends, which seriously affects memory usage and decoding efficiency. Current methods for KV cache eviction typically utilize the last window from the pre-filling phase as queries to compute the KV importance scores for eviction. Although this scheme is simple to implement, it tends to overly focus on local information, potentially leading to the neglect or omission of crucial global information. To mitigate this issue, we propose Judge Q, a novel training method which incorporates a soft token list. This method only tunes the model's embedding layer at a low training cost. By concatenating the soft token list at the end of the input sequence, we train these tokens' attention map to the original input sequence to align with that of the actual decoded tokens. In this way, the queries corresponding to the soft tokens can effectively capture global information and better evaluate the importance of the keys and values within the KV cache, thus maintaining decoding quality when KV cache is evicted. Under the same eviction budget, our method exhibits less performance degradation compared to existing eviction approaches. We validate our approach through experiments conducted on models such as Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3, using benchmarks including LongBench, RULER, and Needle-in-a-Haystack. Results indicate an improvement of approximately 1 point on the LongBench and over 3 points on RULER. This proposed methodology can be seamlessly integrated into existing open-source models with minimal training overhead, thereby enhancing performance in KV cache eviction scenarios.

