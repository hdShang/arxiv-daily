---
layout: default
title: Work-in-Progress: Function-as-Subtask API Replacing Publish/Subscribe for OS-Native DAG Scheduling
---

# Work-in-Progress: Function-as-Subtask API Replacing Publish/Subscribe for OS-Native DAG Scheduling

**arXiv**: [2511.08297v1](https://arxiv.org/abs/2511.08297) | [PDF](https://arxiv.org/pdf/2511.08297.pdf)

**作者**: Takahiro Ishikawa-Aso, Atsushi Yano, Yutaro Kobayashi, Takumi Jin, Yuuki Takano, Shinpei Kato

---

## 💡 一句话要点

**提出Function-as-Subtask API以解决ROS 2中DAG语义未强制的问题**

**关键词**: `实时调度` `DAG任务模型` `ROS 2` `API设计` `语义保证` `操作系统内核`

## 📋 核心要点

1. ROS 2发布/订阅API未强制DAG优先约束，依赖开发者惯例易导致模型失效
2. FasS API将子任务表达为函数，参数和返回值对应边，确保DAG语义
3. 在Rust内核实现DAG原生调度器，评估语义保真度并指导Linux应用

## 📄 摘要（原文）

> The Directed Acyclic Graph (DAG) task model for real-time scheduling finds its primary practical target in Robot Operating System 2 (ROS 2). However, ROS 2's publish/subscribe API leaves DAG precedence constraints unenforced: a callback may publish mid-execution, and multi-input callbacks let developers choose topic-matching policies. Thus preserving DAG semantics relies on conventions; once violated, the model collapses. We propose the Function-as-Subtask (FasS) API, which expresses each subtask as a function whose arguments/return values are the subtask's incoming/outgoing edges. By minimizing description freedom, DAG semantics is guaranteed at the API rather than by programmer discipline. We implement a DAG-native scheduler using FasS on a Rust-based experimental kernel and evaluate its semantic fidelity, and we outline design guidelines for applying FasS to Linux Linux sched_ext.

