---
layout: default
title: In-Context Representation Hijacking
---

# In-Context Representation Hijacking

**arXiv**: [2512.03771v1](https://arxiv.org/abs/2512.03771) | [PDF](https://arxiv.org/pdf/2512.03771.pdf)

**作者**: Itay Yona, Amir Sarid, Michael Karasik, Yossi Gandelsman

---

## 💡 一句话要点

**提出Doublespeak攻击，通过上下文表示劫持绕过大语言模型的安全对齐。**

**关键词**: `表示劫持` `安全对齐` `上下文攻击` `大语言模型` `语义覆盖`

## 📋 核心要点

1. 核心问题：大语言模型的安全对齐在表示层面存在漏洞，允许有害语义被良性词汇隐藏。
2. 方法要点：在上下文示例中系统替换有害关键词为良性词汇，导致内部表示收敛于有害语义。
3. 实验或效果：攻击无需优化，跨模型家族可转移，在Llama-3.3-70B-Instruct上单句上下文覆盖达到74%攻击成功率。

## 📄 摘要（原文）

> We introduce \textbf{Doublespeak}, a simple \emph{in-context representation hijacking} attack against large language models (LLMs). The attack works by systematically replacing a harmful keyword (e.g., \textit{bomb}) with a benign token (e.g., \textit{carrot}) across multiple in-context examples, provided a prefix to a harmful request. We demonstrate that this substitution leads to the internal representation of the benign token converging toward that of the harmful one, effectively embedding the harmful semantics under a euphemism. As a result, superficially innocuous prompts (e.g., ``How to build a carrot?'') are internally interpreted as disallowed instructions (e.g., ``How to build a bomb?''), thereby bypassing the model's safety alignment. We use interpretability tools to show that this semantic overwrite emerges layer by layer, with benign meanings in early layers converging into harmful semantics in later ones. Doublespeak is optimization-free, broadly transferable across model families, and achieves strong success rates on closed-source and open-source systems, reaching 74\% ASR on Llama-3.3-70B-Instruct with a single-sentence context override. Our findings highlight a new attack surface in the latent space of LLMs, revealing that current alignment strategies are insufficient and should instead operate at the representation level.

