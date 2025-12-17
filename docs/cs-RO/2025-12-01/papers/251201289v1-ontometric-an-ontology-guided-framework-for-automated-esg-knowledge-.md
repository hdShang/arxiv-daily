---
layout: default
title: OntoMetric: An Ontology-Guided Framework for Automated ESG Knowledge Graph Construction
---

# OntoMetric: An Ontology-Guided Framework for Automated ESG Knowledge Graph Construction

**arXiv**: [2512.01289v1](https://arxiv.org/abs/2512.01289) | [PDF](https://arxiv.org/pdf/2512.01289.pdf)

**作者**: Mingqin Yu, Fethi Rabhi, Boming Xia, Zhengyi Yang, Felix Tan, Qinghua Lu

---

## 💡 一句话要点

**提出OntoMetric框架，通过本体引导的LLM提取解决ESG监管文档知识图谱构建的不可靠性问题。**

**关键词**: `知识图谱构建` `本体引导提取` `ESG监管文档` `LLM约束` `验证框架` `可持续金融`

## 📋 核心要点

1. 核心问题：ESG监管文档为PDF格式，手动提取不可扩展，无约束LLM提取易产生不一致实体和幻觉关系。
2. 方法要点：采用三阶段流程，包括结构感知分割、本体约束LLM提取和两阶段验证，确保知识图谱的可靠性和可审计性。
3. 实验或效果：在五个ESG标准上评估，语义准确率达65-90%，模式合规率达80-90%，优于基线无约束提取的3-10%。

## 📄 摘要（原文）

> Environmental, Social, and Governance (ESG) disclosure frameworks such as SASB, TCFD, and IFRS S2 require organizations to compute and report numerous metrics for compliance, yet these requirements are embedded in long, unstructured PDF documents that are difficult to interpret, standardize, and audit. Manual extraction is unscalable, while unconstrained large language model (LLM) extraction often produces inconsistent entities, hallucinated relationships, missing provenance, and high validation failure rates. We present OntoMetric, an ontology-guided framework that transforms ESG regulatory documents into validated, AI- and web-ready knowledge graphs. OntoMetric operates through a three-stage pipeline: (1) structure-aware segmentation using table-of-contents boundaries, (2) ontology-constrained LLM extraction that embeds the ESGMKG schema into prompts while enriching entities with semantic fields for downstream reasoning, and (3) two-phase validation that combines LLM-based semantic verification with rule-based schema checking across entity, property, and relationship levels (VR001-VR006). The framework preserves both segment-level and page-level provenance for audit traceability. Evaluated on five ESG standards (SASB Commercial Banks, SASB Semiconductors, TCFD, IFRS S2, AASB S2) totaling 228 pages and 60 segments, OntoMetric achieves 65-90% semantic accuracy and 80-90% schema compliance, compared to 3-10% for baseline unconstrained extraction, at approximately 0.01 to 0.02 USD per validated entity. Our results demonstrate that combining symbolic ontology constraints with neural extraction enables reliable, auditable knowledge graphs suitable for regulatory compliance and web integration, supporting downstream applications such as sustainable-finance analytics, transparency portals, and automated compliance tools.

