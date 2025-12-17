---
layout: default
title: Script Gap: Evaluating LLM Triage on Indian Languages in Native vs Roman Scripts in a Real World Setting
---

# Script Gap: Evaluating LLM Triage on Indian Languages in Native vs Roman Scripts in a Real World Setting

**arXiv**: [2512.10780v1](https://arxiv.org/abs/2512.10780) | [PDF](https://arxiv.org/pdf/2512.10780.pdf)

**作者**: Manurag Khullar, Utkarsh Desai, Poorva Malviya, Aman Dalmia, Zheyuan Ryan Shi

---

## 💡 一句话要点

**评估LLM在印度语言原生与罗马化脚本下的分诊性能，揭示罗马化导致可靠性下降**

**关键词**: `LLM分诊评估` `罗马化脚本影响` `印度语言处理` `临床应用可靠性` `真实世界数据`

## 📋 核心要点

1. 核心问题：LLM在印度临床应用中，用户常用罗马化文本而非原生脚本，现有研究缺乏真实数据评估这种拼写变体对可靠性的影响。
2. 方法要点：基于真实世界数据集，对五种印度语言和尼泊尔语的用户查询，比较LLM在原生与罗马化脚本下的分诊性能。
3. 实验或效果：结果显示罗马化消息性能一致下降，F1分数低5-12点，可能导致近200万额外分诊错误，模型虽能推断语义意图但分类输出脆弱。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly deployed in high-stakes clinical applications in India. In many such settings, speakers of Indian languages frequently communicate using romanized text rather than native scripts, yet existing research rarely evaluates this orthographic variation using real-world data. We investigate how romanization impacts the reliability of LLMs in a critical domain: maternal and newborn healthcare triage. We benchmark leading LLMs on a real-world dataset of user-generated queries spanning five Indian languages and Nepali. Our results reveal consistent degradation in performance for romanized messages, with F1 scores trailing those of native scripts by 5-12 points. At our partner maternal health organization in India, this gap could cause nearly 2 million excess errors in triage. Crucially, this performance gap by scripts is not due to a failure in clinical reasoning. We demonstrate that LLMs often correctly infer the semantic intent of romanized queries. Nevertheless, their final classification outputs remain brittle in the presence of orthographic noise in romanized inputs. Our findings highlight a critical safety blind spot in LLM-based health systems: models that appear to understand romanized input may still fail to act on it reliably.

