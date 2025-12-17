---
layout: default
title: To Err Is Human: Systematic Quantification of Errors in Published AI Papers via LLM Analysis
---

# To Err Is Human: Systematic Quantification of Errors in Published AI Papers via LLM Analysis

**arXiv**: [2512.05925v1](https://arxiv.org/abs/2512.05925) | [PDF](https://arxiv.org/pdf/2512.05925.pdf)

**作者**: Federico Bianchi, Yongchan Kwon, Zachary Izzo, Linjun Zhang, James Zou

---

## 💡 一句话要点

**提出基于GPT-5的论文正确性检查器，系统量化AI顶会论文中的客观错误**

**关键词**: `论文错误检测` `GPT-5应用` `可复现性研究` `客观错误量化` `AI顶会分析`

## 📋 核心要点

1. 核心问题：AI顶会论文中存在客观错误，可能影响后续研究和可复现性
2. 方法要点：使用GPT-5构建检查器，专注于公式、推导、计算等可验证错误
3. 实验或效果：在NeurIPS等会议论文中，错误数量随时间增加，检查器精度达83.2%，可修正75.8%的错误

## 📄 摘要（原文）

> How many mistakes do published AI papers contain? Peer-reviewed publications form the foundation upon which new research and knowledge are built. Errors that persist in the literature can propagate unnoticed, creating confusion in follow-up studies and complicating reproducibility. The accelerating pace of research and the increasing demands on the peer-review system make such mistakes harder to detect and avoid. To address this, we developed a Paper Correctness Checker based on GPT-5 to systematically identify mistakes in papers previously published at top AI conferences and journals. Our analysis focuses on objective mistakes-e.g., errors in formulas, derivations, calculations, figures, and tables-that have a clearly verifiable ground truth. We intentionally exclude subjective considerations such as novelty, importance, or writing quality. We find that published papers contain a non-negligible number of objective mistakes and that the average number of mistakes per paper has increased over time-from 3.8 in NeurIPS 2021 to 5.9 in NeurIPS 2025 (55.3% increase); from 4.1 in ICLR 2018 to 5.2 in ICLR 2025; and from 5.0 in TMLR 2022/23 to 5.5 in TMLR 2025. Human experts reviewed 316 potential mistakes identified by the AI Checker and confirmed that 263 were actual mistakes, corresponding to a precision of 83.2%. While most identified issues are relatively minor, correcting them would reduce confusion in the literature and strengthen reproducibility. The AI Checker also surfaced potentially more substantive mistakes that could affect the interpretation of results. Moreover, we show that the AI Checker can propose correct fixes for 75.8% of the identified mistakes. Overall, this study highlights the potential of frontier LLMs to detect and correct objective mistakes in published papers, helping to establish a firmer foundation of knowledge.

