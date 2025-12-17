---
layout: default
title: FineVision: Open Data Is All You Need
---

# FineVision: Open Data Is All You Need

**arXiv**: [2510.17269v1](https://arxiv.org/abs/2510.17269) | [PDF](https://arxiv.org/pdf/2510.17269.pdf)

**作者**: Luis Wiedmann, Orr Zohar, Amir Mahla, Xiaohan Wang, Rui Li, Thibaud Frere, Leandro von Werra, Aritra Roy Gosthipaty, Andrés Marafioti

---

## 💡 一句话要点

**提出FineVision大规模开放数据集以解决视觉语言模型数据碎片化问题**

**关键词**: `视觉语言模型` `数据集构建` `数据去重` `数据去污染` `半自动化流程` `开放数据`

## 📋 核心要点

1. 视觉语言模型发展受限于公共数据集不一致和污染问题
2. 通过半自动化流程统一200多源数据，并进行去重和去污染处理
3. 基于FineVision训练的模型在广泛评估中优于现有开放数据集模型

## 📄 摘要（原文）

> The advancement of vision-language models (VLMs) is hampered by a fragmented
> landscape of inconsistent and contaminated public datasets. We introduce
> FineVision, a meticulously collected, curated, and unified corpus of 24 million
> samples - the largest open resource of its kind. We unify more than 200 sources
> into 185 subsets via a semi-automated, human-in-the-loop pipeline: automation
> performs bulk ingestion and schema mapping, while reviewers audit mappings and
> spot-check outputs to verify faithful consumption of annotations, appropriate
> formatting and diversity, and safety; issues trigger targeted fixes and
> re-runs. The workflow further applies rigorous de-duplication within and across
> sources and decontamination against 66 public benchmarks. FineVision also
> encompasses agentic/GUI tasks with a unified action space; reviewers validate
> schemas and inspect a sample of trajectories to confirm executable fidelity.
> Models trained on FineVision consistently outperform those trained on existing
> open mixtures across a broad evaluation suite, underscoring the benefits of
> scale, data hygiene, and balanced automation with human oversight. We release
> the corpus and curation tools to accelerate data-centric VLM research.

