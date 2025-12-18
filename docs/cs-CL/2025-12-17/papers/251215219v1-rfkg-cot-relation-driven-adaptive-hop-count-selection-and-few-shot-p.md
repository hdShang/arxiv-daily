---
layout: default
title: RFKG-CoT: Relation-Driven Adaptive Hop-count Selection and Few-Shot Path Guidance for Knowledge-Aware QA
---

# RFKG-CoT: Relation-Driven Adaptive Hop-count Selection and Few-Shot Path Guidance for Knowledge-Aware QA

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15219" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15219v1</a>
  <a href="https://arxiv.org/pdf/2512.15219.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15219v1" onclick="toggleFavorite(this, '2512.15219v1', 'RFKG-CoT: Relation-Driven Adaptive Hop-count Selection and Few-Shot Path Guidance for Knowledge-Aware QA')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chao Zhang, Minghan Li, Tianrui Lv, Guodong Zhou

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-17

**备注**: 9pages, 5 figures, accepted by AAAI 2026

---

## 💡 一句话要点

**RFKG-CoT：关系驱动的自适应跳数选择与少样本路径引导，提升知识图谱问答效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱问答` `大型语言模型` `关系驱动` `自适应跳数选择` `少样本学习` `路径引导` `知识推理`

## 📋 核心要点

1. 现有知识图谱问答方法在选择推理路径的跳数时存在僵化问题，且对推理路径的利用不足。
2. RFKG-CoT通过关系驱动的自适应跳数选择和少样本路径引导，动态调整推理步骤并增强LLM对推理路径的理解。
3. 实验结果表明，RFKG-CoT在多个知识图谱问答基准上显著提升了准确率，最高提升达14.7个百分点。

## 📝 摘要（中文）

大型语言模型（LLMs）由于参数知识的局限性，在知识密集型问答中经常产生幻觉。现有的KG-CoT等方法通过整合知识图谱（KG）路径来提高可靠性，但存在跳数选择僵化（仅由问题驱动）和推理路径利用不足（缺乏指导）的问题。为了解决这些问题，我们提出了RFKG-CoT：首先，它用关系驱动的自适应跳数选择器取代了僵化的跳数选择器，通过激活KG关系（例如，直接“兄弟”关系为1跳，间接“父子”链为2跳）来动态调整推理步骤，并通过关系掩码进行形式化。其次，它引入了一种基于CoT（思考）的少样本上下文学习路径引导机制，以“问题-路径-答案”格式构建示例，以增强LLM理解推理路径的能力。在四个KGQA基准上的实验表明，RFKG-CoT相对于KG-CoT，在WebQSP上使用Llama2-7B时，准确率提高了高达14.7个百分点。消融实验证实，跳数选择器和路径提示是互补的，共同将KG证据转化为更可靠的答案。

## 🔬 方法详解

**问题定义**：论文旨在解决知识图谱问答（KGQA）中，大型语言模型（LLMs）由于自身知识的局限性而产生幻觉的问题。现有方法，如KG-CoT，虽然利用知识图谱（KG）路径进行推理，但其跳数选择策略过于僵化，仅依赖问题本身，无法根据不同关系类型调整推理深度。此外，现有方法对推理路径的利用不足，缺乏对LLM的有效引导，导致推理效果不佳。

**核心思路**：RFKG-CoT的核心思路是使LLM能够根据知识图谱中关系的不同，自适应地选择推理路径的跳数，并利用少样本学习来引导LLM更好地理解和利用推理路径。通过关系驱动的跳数选择，模型可以更灵活地探索知识图谱，找到更合适的推理路径。通过少样本路径引导，模型可以学习到如何从知识图谱中提取有用的信息，并将其用于回答问题。

**技术框架**：RFKG-CoT的整体框架包括以下几个主要模块：1) 问题编码模块：将输入问题编码成向量表示。2) 关系驱动的自适应跳数选择器：根据问题和知识图谱中的关系，动态选择推理路径的跳数。3) 知识图谱路径检索模块：根据选择的跳数，从知识图谱中检索相关的推理路径。4) 少样本路径引导模块：利用少样本学习，引导LLM理解和利用检索到的推理路径。5) 答案生成模块：根据问题和推理路径，生成最终答案。

**关键创新**：RFKG-CoT的关键创新在于：1) 提出了关系驱动的自适应跳数选择器，能够根据知识图谱中关系的不同，动态调整推理路径的跳数，从而更灵活地探索知识图谱。2) 引入了少样本路径引导机制，通过构建“问题-路径-答案”格式的示例，增强LLM对推理路径的理解和利用能力。

**关键设计**：关系驱动的自适应跳数选择器使用关系掩码来形式化不同关系类型对应的跳数。例如，对于直接关系（如“兄弟”），使用1跳；对于间接关系（如“父子”），使用2跳。少样本路径引导模块通过选择少量高质量的“问题-路径-答案”示例，并将其作为上下文输入LLM，以引导LLM更好地理解和利用推理路径。具体示例的选择策略未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15219v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15219v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15219v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RFKG-CoT在四个知识图谱问答基准上均取得了显著的性能提升。特别是在WebQSP数据集上，使用Llama2-7B模型时，RFKG-CoT相对于KG-CoT，准确率提高了高达14.7个百分点。消融实验进一步验证了关系驱动的自适应跳数选择器和少样本路径引导机制的有效性和互补性。

## 🎯 应用场景

RFKG-CoT可应用于各种需要知识推理的问答场景，例如智能客服、知识库问答、教育辅导等。该研究能够提升LLM在知识密集型任务中的可靠性和准确性，减少幻觉的产生，具有重要的实际应用价值。未来，该方法可以进一步扩展到更复杂的知识图谱和推理场景中，例如多跳推理、逻辑推理等。

## 📄 摘要（原文）

> Large language models (LLMs) often generate hallucinations in knowledge-intensive QA due to parametric knowledge limitations. While existing methods like KG-CoT improve reliability by integrating knowledge graph (KG) paths, they suffer from rigid hop-count selection (solely question-driven) and underutilization of reasoning paths (lack of guidance). To address this, we propose RFKG-CoT: First, it replaces the rigid hop-count selector with a relation-driven adaptive hop-count selector that dynamically adjusts reasoning steps by activating KG relations (e.g., 1-hop for direct "brother" relations, 2-hop for indirect "father-son" chains), formalized via a relation mask. Second, it introduces a few-shot in-context learning path guidance mechanism with CoT (think) that constructs examples in a "question-paths-answer" format to enhance LLMs' ability to understand reasoning paths. Experiments on four KGQA benchmarks show RFKG-CoT improves accuracy by up to 14.7 pp (Llama2-7B on WebQSP) over KG-CoT. Ablations confirm the hop-count selector and the path prompt are complementary, jointly transforming KG evidence into more faithful answers.

