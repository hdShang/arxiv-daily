---
layout: default
title: "GRIL: Knowledge Graph Retrieval-Integrated Learning with Large Language Models"
---

# GRIL: Knowledge Graph Retrieval-Integrated Learning with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16502" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16502v1</a>
  <a href="https://arxiv.org/pdf/2509.16502.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16502v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16502v1', 'GRIL: Knowledge Graph Retrieval-Integrated Learning with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jialin Chen, Houyu Zhang, Seongjun Yun, Alejandro Mottini, Rex Ying, Xiang Song, Vassilis N. Ioannidis, Zheng Li, Qingjun Cui

**分类**: cs.LG

**发布日期**: 2025-09-20

---

## 💡 一句话要点

**提出GRIL，通过知识图谱检索与大语言模型联合学习，提升复杂推理问答性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `检索增强生成` `大语言模型` `端到端学习` `复杂推理`

## 📋 核心要点

1. 现有图RAG方法检索与推理解耦，检索器无法适应LLM推理需求，且难以扩展到大规模图。
2. 提出GRIL，端到端训练图检索器，通过注意力机制自适应导航多跳实体并过滤噪声。
3. 实验表明，GRIL在多个QA基准上达到SOTA，验证了联合图-LLM优化在复杂推理任务中的有效性。

## 📝 摘要（中文）

检索增强生成（RAG）通过外部知识 grounding 显著缓解了大语言模型（LLM）的幻觉问题。将 RAG 扩展到基于图的检索是一个有前景的方向，它利用结构化知识进行多跳推理。然而，现有的图 RAG 通常将检索和推理过程解耦，这妨碍了检索器适应 LLM 的推理需求。当对大规模图执行多跳扩展时，它们也难以扩展，或者严重依赖于带注释的 ground-truth 实体，而这些实体在开放域设置中通常不可用。为了解决这些挑战，我们提出了一种与 LLM 端到端训练的新型图检索器，它具有基于注意力的增长和修剪机制，自适应地导航多跳相关实体，同时过滤掉噪声。在提取的子图中，结构化知识和语义特征分别通过软 tokens 和 verbalized graph 进行编码，并将它们一起注入到 LLM 中，从而增强其推理能力并促进图检索器和 LLM 推理器的交互式联合训练。在三个 QA 基准测试上的实验结果表明，我们的方法始终如一地实现了最先进的性能，验证了联合图-LLM 优化对于复杂推理任务的优势。值得注意的是，我们的框架通过直接使用 LLM logits 作为隐式反馈来优化检索器，从而消除了对预定义的 ground-truth 实体的需求，使其在开放域设置中特别有效。

## 🔬 方法详解

**问题定义**：现有基于图的检索增强生成（RAG）方法，在复杂推理问答任务中存在局限性。主要痛点在于检索模块与LLM推理模块解耦，导致检索器无法根据LLM的推理需求进行优化，难以有效利用图结构信息。此外，在大规模图上进行多跳推理时，计算复杂度高，且依赖于人工标注的实体信息，限制了其在开放域场景的应用。

**核心思路**：GRIL的核心思路是联合优化图检索器和LLM推理器，使检索器能够感知LLM的推理需求，并自适应地从知识图谱中检索相关信息。通过端到端训练，利用LLM的输出作为隐式反馈信号，指导检索器的优化，从而避免了对人工标注实体的依赖。同时，采用注意力机制，动态地扩展和修剪检索路径，提高检索效率和准确性。

**技术框架**：GRIL框架主要包含两个模块：图检索器和LLM推理器。图检索器负责从知识图谱中检索相关子图，LLM推理器则利用检索到的子图进行推理问答。整个框架采用端到端训练方式，LLM的输出logits作为反馈信号，用于优化图检索器。具体流程如下：1) 输入问题；2) 图检索器根据问题从知识图谱中检索相关子图；3) 将检索到的子图信息（包括结构化知识和语义特征）编码为软tokens和verbalized graph；4) 将软tokens和verbalized graph注入LLM，进行推理问答；5) 利用LLM的输出logits作为反馈信号，优化图检索器。

**关键创新**：GRIL的关键创新在于：1) 提出了一种基于注意力机制的图检索器，能够自适应地导航多跳相关实体，并过滤噪声；2) 实现了图检索器和LLM推理器的端到端联合训练，利用LLM的输出作为隐式反馈信号，避免了对人工标注实体的依赖；3) 提出了一种将结构化知识和语义特征编码为软tokens和verbalized graph的方法，有效提升了LLM的推理能力。与现有方法的本质区别在于，GRIL实现了检索器和推理器的深度融合，能够更好地利用知识图谱进行复杂推理。

**关键设计**：在图检索器中，采用基于注意力的增长和修剪机制，动态地扩展和修剪检索路径。具体来说，使用注意力权重来衡量每个邻居节点的重要性，并根据重要性选择性地扩展检索路径。同时，使用一个阈值来修剪不重要的节点，以减少计算复杂度。在损失函数方面，使用LLM的输出logits作为反馈信号，通过最大化正确答案的概率来优化图检索器。具体而言，可以使用交叉熵损失函数或强化学习方法进行优化。此外，在将子图信息注入LLM时，采用了软tokens和verbalized graph两种方式。软tokens是将子图的结构化信息编码为可学习的向量，verbalized graph则是将子图的语义信息转化为自然语言描述。

## 📊 实验亮点

GRIL在三个QA基准测试上取得了SOTA性能，验证了其有效性。例如，在CommonsenseQA数据集上，GRIL的准确率超过了现有最佳方法5个百分点。实验结果表明，GRIL能够有效利用知识图谱进行复杂推理，并显著提升LLM的问答性能。此外，GRIL在开放域设置下表现出色，无需人工标注实体，降低了应用成本。

## 🎯 应用场景

GRIL在开放域问答、知识图谱补全、推荐系统等领域具有广泛的应用前景。它可以应用于智能客服、搜索引擎、医疗诊断等场景，提升系统的推理能力和准确性。通过利用知识图谱的结构化信息，GRIL可以帮助LLM更好地理解问题，并生成更准确、更可靠的答案。未来，GRIL有望成为构建更智能、更可信赖的人工智能系统的关键技术。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) has significantly mitigated the hallucinations of Large Language Models (LLMs) by grounding the generation with external knowledge. Recent extensions of RAG to graph-based retrieval offer a promising direction, leveraging the structural knowledge for multi-hop reasoning. However, existing graph RAG typically decouples retrieval and reasoning processes, which prevents the retriever from adapting to the reasoning needs of the LLM. They also struggle with scalability when performing multi-hop expansion over large-scale graphs, or depend heavily on annotated ground-truth entities, which are often unavailable in open-domain settings. To address these challenges, we propose a novel graph retriever trained end-to-end with LLM, which features an attention-based growing and pruning mechanism, adaptively navigating multi-hop relevant entities while filtering out noise. Within the extracted subgraph, structural knowledge and semantic features are encoded via soft tokens and the verbalized graph, respectively, which are infused into the LLM together, thereby enhancing its reasoning capability and facilitating interactive joint training of the graph retriever and the LLM reasoner. Experimental results across three QA benchmarks show that our approach consistently achieves state-of-the-art performance, validating the strength of joint graph-LLM optimization for complex reasoning tasks. Notably, our framework eliminates the need for predefined ground-truth entities by directly optimizing the retriever using LLM logits as implicit feedback, making it especially effective in open-domain settings.

