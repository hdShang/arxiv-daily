---
layout: default
title: "When to Trust Context: Self-Reflective Debates for Context Reliability"
---

# When to Trust Context: Self-Reflective Debates for Context Reliability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06020" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06020v1</a>
  <a href="https://arxiv.org/pdf/2506.06020.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06020v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06020v1', 'When to Trust Context: Self-Reflective Debates for Context Reliability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeqi Zhou, Fang Wu, Shayan Talaei, Haokai Zhao, Cheng Meixin, Tinson Xu, Amin Saberi, Yejin Choi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-06

**🔗 代码/项目**: [GITHUB](https://github.com/smiles724/Self-Reflective-Debates)

---

## 💡 一句话要点

**提出自反辩论框架以提升上下文可靠性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `上下文可靠性` `自反辩论` `大型语言模型` `多代理系统` `自然语言处理`

## 📋 核心要点

1. 现有大型语言模型在处理上下文时，常出现知识与上下文冲突，导致不准确的回答或幻觉现象。
2. 本文提出的SR-DCR框架通过自信度与多代理辩论相结合，旨在有效裁决上下文的可靠性。
3. 实验结果显示，SR-DCR在ClashEval基准测试中显著提升了对误导性上下文的鲁棒性，同时保持了在可信输入上的准确性。

## 📝 摘要（中文）

大型语言模型在处理上下文输入时，常常面临其参数知识与上下文之间的冲突，导致事实不一致或幻觉现象。为此，本文提出了一种轻量级框架——自反辩论上下文可靠性（SR-DCR），该框架将令牌级自信度与不对称多代理辩论相结合，以裁决此类冲突。该框架中，缺乏上下文的批评者挑战基于给定段落进行辩护的辩护者，评判模型则评估辩论并确定上下文的可靠性。最终答案通过结合评判结果与模型自信度进行选择。实验结果表明，SR-DCR在抵御误导性上下文方面表现出色，同时在可信输入上保持准确性，相较于经典辩论和仅依赖自信度的基线方法，具有更小的计算开销。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在面对上下文输入时，因知识与上下文冲突而导致的事实不一致和幻觉问题。现有方法在处理此类冲突时，往往缺乏有效的机制来评估上下文的可靠性。

**核心思路**：SR-DCR框架通过引入自信度评估与多代理辩论机制，允许模型在缺乏上下文的情况下进行有效的自我反思和判断，从而提高上下文的可靠性。

**技术框架**：该框架主要由三个模块组成：批评者、辩护者和评判模型。批评者在没有上下文的情况下提出质疑，辩护者则基于给定段落进行辩护，评判模型负责评估辩论结果并判断上下文的可靠性。

**关键创新**：SR-DCR的创新在于将自信度与辩论机制相结合，形成了一种新的上下文评估方式。这种方法与传统的单一自信度评估或简单辩论机制相比，能够更全面地考虑上下文的多维度信息。

**关键设计**：在设计上，SR-DCR采用了轻量级的计算架构，确保在保持高效性的同时，能够处理复杂的辩论过程。具体的参数设置和损失函数设计尚未详细披露，需进一步研究。

## 📊 实验亮点

在ClashEval基准测试中，SR-DCR显著提高了对误导性上下文的鲁棒性，准确率在可信输入上保持不变。与经典辩论和仅依赖自信度的基线方法相比，SR-DCR在计算开销上表现出色，展示了其高效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、对话系统以及任何需要处理复杂上下文的自然语言处理任务。通过提升上下文的可靠性，SR-DCR能够有效减少模型的错误回答，增强用户体验，未来可能在教育、客服等领域产生深远影响。

## 📄 摘要（原文）

> Large language models frequently encounter conflicts between their parametric knowledge and contextual input, often resulting in factual inconsistencies or hallucinations. We propose Self-Reflective Debate for Contextual Reliability (SR-DCR), a lightweight framework that integrates token-level self-confidence with an asymmetric multi-agent debate to adjudicate such conflicts. A critic, deprived of context, challenges a defender who argues from the given passage; a judge model evaluates the debate and determines the context's reliability. The final answer is selected by combining the verdict with model confidence. Experiments on the ClashEval benchmark demonstrate that SR-DCR consistently enhances robustness to misleading context while maintaining accuracy on trustworthy inputs, outperforming both classical debate and confidence-only baselines with minimal computational overhead. The code is available at https://github.com/smiles724/Self-Reflective-Debates.

