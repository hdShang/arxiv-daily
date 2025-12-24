---
layout: default
title: "DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models"
---

# DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13702" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13702v1</a>
  <a href="https://arxiv.org/pdf/2509.13702.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13702v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13702v1', 'DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Zheng

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-17

---

## 💡 一句话要点

**提出DSCC-HS框架以主动抑制大型语言模型的幻觉现象**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `幻觉抑制` `动态自我强化` `事实一致性` `自然语言处理` `对抗性训练` `推理机制`

## 📋 核心要点

1. 现有方法如RAG在处理大型语言模型的幻觉现象时多为反应式，难以有效抑制幻觉的产生。
2. DSCC-HS框架通过动态自我强化校准，在自回归解码过程中主动干预，利用事实对齐代理和幻觉检测代理进行实时引导。
3. 实验结果显示，DSCC-HS在TruthfulQA上实现了99.2%的事实一致率，在BioGEN基准上获得了46.50的FActScore，表现优异。

## 📝 摘要（中文）

大型语言模型（LLM）的幻觉现象是其可靠部署的一大障碍。当前的方法如检索增强生成（RAG）往往是反应式的。我们提出了动态自我强化校准框架（DSCC-HS），这是一个新颖的主动框架，在自回归解码过程中进行干预。DSCC-HS受到双过程认知理论的启发，利用一个紧凑的代理模型，分别作为事实对齐代理（FAP）和幻觉检测代理（HDP）进行对抗性训练。在推理过程中，这些代理通过在每个解码步骤注入实时引导向量（FAP和HDP logits之间的差异）动态引导大型目标模型。该即插即用的方法无需对目标模型进行修改。我们的实验表明，DSCC-HS在TruthfulQA和BioGEN上达到了最先进的性能，在TruthfulQA上达到了99.2%的事实一致率（FCR），在长文本BioGEN基准上获得了最高的FActScore 46.50。这些结果验证了DSCC-HS作为增强LLM事实性的原则性和高效解决方案。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在生成过程中出现的幻觉现象，现有方法如RAG往往是反应式的，无法有效预防幻觉的发生。

**核心思路**：DSCC-HS框架通过引入动态自我强化校准机制，利用两个代理模型（FAP和HDP）在解码过程中实时干预，从而主动抑制幻觉现象的产生。

**技术框架**：DSCC-HS的整体架构包括两个主要模块：事实对齐代理（FAP）和幻觉检测代理（HDP）。在推理阶段，这两个代理模型生成的logits差异作为引导向量，动态影响目标模型的输出。

**关键创新**：DSCC-HS的主要创新在于其主动干预机制，通过实时引导向量的注入，显著提升了大型语言模型的事实一致性，与传统的反应式方法形成鲜明对比。

**关键设计**：在模型设计上，FAP和HDP分别经过对抗性训练，以确保其在推理过程中能够有效识别和校正幻觉现象。引导向量的计算方式和注入策略是该方法的关键技术细节。

## 📊 实验亮点

DSCC-HS在TruthfulQA上达到了99.2%的事实一致率，显著高于现有基线；在BioGEN基准上获得了46.50的FActScore，展示了其在长文本生成中的优越性能。这些结果表明，DSCC-HS在幻觉抑制方面具有显著的效果提升。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在需要高可靠性的自然语言处理任务中，如医疗文本生成、法律文书撰写和新闻报道等领域。通过提高大型语言模型的事实一致性，DSCC-HS能够增强这些系统的可信度和实用性，推动其在实际应用中的落地。

## 📄 摘要（原文）

> Large Language Model (LLM) hallucination is a significant barrier to their reliable deployment. Current methods like Retrieval-Augmented Generation (RAG) are often reactive. We introduce **Dynamic Self-reinforcing Calibration for Hallucination Suppression (DSCC-HS)**, a novel, proactive framework that intervenes during autoregressive decoding. Inspired by dual-process cognitive theory, DSCC-HS uses a compact proxy model, trained in adversarial roles as a Factual Alignment Proxy (FAP) and a Hallucination Detection Proxy (HDP). During inference, these proxies dynamically steer a large target model by injecting a real-time steering vector, which is the difference between FAP and HDP logits, at each decoding step. This plug-and-play approach requires no modification to the target model. Our experiments on TruthfulQA and BioGEN show DSCC-HS achieves state-of-the-art performance. On TruthfulQA, it reached a 99.2% Factual Consistency Rate (FCR). On the long-form BioGEN benchmark, it attained the highest FActScore of 46.50. These results validate DSCC-HS as a principled and efficient solution for enhancing LLM factuality.

