---
layout: default
title: Scaling Text2SQL via LLM-efficient Schema Filtering with Functional Dependency Graph Rerankers
---

# Scaling Text2SQL via LLM-efficient Schema Filtering with Functional Dependency Graph Rerankers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16083" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16083v1</a>
  <a href="https://arxiv.org/pdf/2512.16083.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16083v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16083v1', 'Scaling Text2SQL via LLM-efficient Schema Filtering with Functional Dependency Graph Rerankers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thanh Dat Hoang, Thanh Tam Nguyen, Thanh Trung Huynh, Hongzhi Yin, Quoc Viet Hung Nguyen

**分类**: cs.DB, cs.AI, cs.HC, cs.LG

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/thanhdath/grast-sql)

---

## 💡 一句话要点

**提出GRaST，通过LLM高效的模式过滤和函数依赖图重排序，扩展Text2SQL到大规模数据库。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Text2SQL` `大型语言模型` `模式过滤` `函数依赖图` `图Transformer` `Steiner树` `数据库查询`

## 📋 核心要点

1. 现有Text2SQL系统在处理大规模数据库时，由于LLM上下文长度限制，无法有效利用完整数据库模式信息。
2. GRaST框架通过查询感知的LLM编码器、函数依赖图Transformer和Steiner树启发式算法，实现高效的模式过滤和子模式选择。
3. 实验表明，GRaST在保持低延迟的同时，实现了接近完美的召回率和更高的精度，并可扩展到包含大量列的数据库模式。

## 📝 摘要（中文）

大多数现代Text2SQL系统在提示大型语言模型（LLM）时，会将整个模式（主要是列信息）与用户的问题一起提供。虽然这种方法在小型数据库上有效，但对于超出LLM上下文限制的真实模式则会失效，即使是商业模型也是如此。最近的Spider 2.0基准测试就是一个例子，它包含数百个表和数万列，现有系统经常崩溃。目前的缓解措施要么依赖于代价高昂的多步骤提示流程，要么通过独立地将列与用户的问题进行排序来过滤列，忽略了列间的结构。为了扩展现有系统，我们引入了GRaST，这是一个开源的、LLM高效的模式过滤框架，它通过以下方式压缩Text2SQL提示：（i）使用富含值和元数据的查询感知LLM编码器对列进行排序，（ii）通过函数依赖关系上的轻量级图Transformer对互连的列进行重排序，以及（iii）使用Steiner树启发式算法选择一个保持连通性的子模式。在真实数据集上的实验表明，GRaST实现了接近完美的召回率和比CodeS、SchemaExP、Qwen重排序器和嵌入检索器更高的精度，同时保持了亚秒级的中值延迟，并可扩展到具有23,000+列的模式。我们的源代码可在https://github.com/thanhdath/grast-sql 获得。

## 🔬 方法详解

**问题定义**：现有Text2SQL系统在处理大规模数据库时，需要将整个数据库模式信息输入到LLM中，但由于LLM上下文长度的限制，导致系统性能下降甚至崩溃。现有的解决方法要么依赖于多步骤的提示，增加了计算成本，要么忽略了列之间的依赖关系，导致过滤后的模式信息不完整。

**核心思路**：GRaST的核心思路是通过高效的模式过滤，选择与用户查询相关的子模式，从而减少LLM需要处理的信息量。同时，利用函数依赖图来捕捉列之间的关系，保证选择的子模式包含完整的语义信息。

**技术框架**：GRaST框架包含三个主要阶段：（1）列排序：使用查询感知的LLM编码器对数据库中的列进行排序，评估其与用户查询的相关性。（2）列重排序：利用函数依赖图Transformer对互连的列进行重排序，考虑列之间的依赖关系。（3）子模式选择：使用Steiner树启发式算法选择一个保持连通性的子模式，作为LLM的输入。

**关键创新**：GRaST的关键创新在于结合了查询感知的LLM编码器和函数依赖图Transformer，从而在保证模式信息完整性的同时，实现了高效的模式过滤。此外，使用Steiner树启发式算法选择子模式，进一步提高了系统的效率。

**关键设计**：查询感知的LLM编码器通过融合列的值和元数据信息，提高了列排序的准确性。函数依赖图Transformer利用图结构来捕捉列之间的依赖关系，从而更好地进行列重排序。Steiner树启发式算法通过寻找连接关键列的最小代价树，保证选择的子模式包含完整的语义信息。

## 📊 实验亮点

在真实数据集上的实验表明，GRaST实现了接近完美的召回率，并且精度高于CodeS、SchemaExP、Qwen重排序器和嵌入检索器等基线方法。同时，GRaST保持了亚秒级的中值延迟，并可扩展到具有超过23,000列的模式，证明了其在大规模数据库上的有效性和高效性。

## 🎯 应用场景

GRaST框架可应用于各种需要处理大规模数据库的Text2SQL系统，例如智能客服、数据分析平台和商业智能工具。通过提高Text2SQL系统处理大规模数据库的能力，可以帮助用户更方便地从海量数据中获取所需信息，从而提高工作效率和决策质量。未来，该技术还可以扩展到其他需要处理大规模结构化数据的领域。

## 📄 摘要（原文）

> Most modern Text2SQL systems prompt large language models (LLMs) with entire schemas -- mostly column information -- alongside the user's question. While effective on small databases, this approach fails on real-world schemas that exceed LLM context limits, even for commercial models. The recent Spider 2.0 benchmark exemplifies this with hundreds of tables and tens of thousands of columns, where existing systems often break. Current mitigations either rely on costly multi-step prompting pipelines or filter columns by ranking them against user's question independently, ignoring inter-column structure. To scale existing systems, we introduce \toolname, an open-source, LLM-efficient schema filtering framework that compacts Text2SQL prompts by (i) ranking columns with a query-aware LLM encoder enriched with values and metadata, (ii) reranking inter-connected columns via a lightweight graph transformer over functional dependencies, and (iii) selecting a connectivity-preserving sub-schema with a Steiner-tree heuristic. Experiments on real datasets show that \toolname achieves near-perfect recall and higher precision than CodeS, SchemaExP, Qwen rerankers, and embedding retrievers, while maintaining sub-second median latency and scaling to schemas with 23,000+ columns. Our source code is available at https://github.com/thanhdath/grast-sql.

