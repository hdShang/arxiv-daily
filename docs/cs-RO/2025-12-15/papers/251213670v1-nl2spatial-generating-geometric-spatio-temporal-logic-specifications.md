---
layout: default
title: NL2SpaTiaL: Generating Geometric Spatio-Temporal Logic Specifications from Natural Language for Manipulation Tasks
---

# NL2SpaTiaL: Generating Geometric Spatio-Temporal Logic Specifications from Natural Language for Manipulation Tasks

**arXiv**: [2512.13670v1](https://arxiv.org/abs/2512.13670) | [PDF](https://arxiv.org/pdf/2512.13670.pdf)

**作者**: Licheng Luo, Yu Xia, Kaier Liang, Mingyu Cai

---

## 💡 一句话要点

**提出NL2SpaTiaL框架，从自然语言生成几何时空逻辑规范以解决机器人操作任务中的空间关系建模问题。**

**关键词**: `时空逻辑生成` `自然语言处理` `机器人操作` `数据集构建` `语义验证`

## 📋 核心要点

1. 核心问题：现有方法依赖标准时序逻辑，忽略对象级交互和分层空间关系，导致机器人操作任务建模不足。
2. 方法要点：引入数据集生成框架，合成SpaTiaL规范并通过确定性回译转换为自然语言描述，构建NL2SpaTiaL数据集。
3. 实验或效果：基于SpaTiaL的表示在操作任务中实现更可解释、可验证和组合的指令遵循，提升任务性能。

## 📄 摘要（原文）

> Spatio-Temporal Logic (SpaTiaL) offers a principled formalism for expressing geometric spatial requirements-an essential component of robotic manipulation, where object locations, neighborhood relations, pose constraints, and interactions directly determine task success. Yet prior works have largely relied on standard temporal logic (TL), which models only robot trajectories and overlooks object-level interactions. Existing datasets built from randomly generated TL formulas paired with natural-language descriptions therefore cover temporal operators but fail to represent the layered spatial relations that manipulation tasks depend on. To address this gap, we introduce a dataset generation framework that synthesizes SpaTiaL specifications and converts them into natural-language descriptions through a deterministic, semantics-preserving back-translation procedure. This pipeline produces the NL2SpaTiaL dataset, aligning natural language with multi-level spatial relations and temporal objectives to reflect the compositional structure of manipulation tasks. Building on this foundation, we propose a translation-verification framework equipped with a language-based semantic checker that ensures the generated SpaTiaL formulas faithfully encode the semantics specified by the input description. Experiments across a suite of manipulation tasks show that SpaTiaL-based representations yield more interpretable, verifiable, and compositional grounding for instruction following. Project website: https://sites.google.com/view/nl2spatial

